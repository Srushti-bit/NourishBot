from .aliases import alias_lookup, UNRESOLVED, CANONICAL_OVERRIDES
from .matcher import FoodMatcher
from .selector import FoodSelector
from .db_index import FoodDBIndex


class FoodMatch:
    def __init__(self, input_name, canonical_name, confidence, method):
        self.input_name = input_name
        self.canonical_name = canonical_name
        self.confidence = confidence
        self.method = method

    def __repr__(self):
        return (
            f"FoodMatch({self.input_name} → "
            f"{self.canonical_name}, {self.confidence}, {self.method})"
        )


class FoodResolver:
    def __init__(self, db_path: str):
        self.db_index = FoodDBIndex(db_path)
        self.db_index.load()

        self.matcher = FoodMatcher(self.db_index)
        self.selector = FoodSelector()

    def resolve_food(self, food: str) -> FoodMatch:
        raw = food.lower().strip()

        # -----------------------------
        # 0. CANONICAL OVERRIDE LAYER
        # -----------------------------
        override = CANONICAL_OVERRIDES.get(raw)
        if override:
            row = self.db_index.get_by_exact_name(override)
            if row:
                return FoodMatch(
                    raw,
                    row.get("normalized_name"),
                    1.0,
                    "canonical_override",
                )

        # -----------------------------
        # NORMALIZATION
        # -----------------------------
        for word in ["grilled", "fried", "boiled", "roasted", "baked"]:
            raw = raw.replace(word, "").strip()

        # -----------------------------
        # DEBUG
        # -----------------------------
        print(f"\nINPUT TO ALIAS: {raw}")

        # -----------------------------
        # 1. ALIAS LAYER
        # -----------------------------
        alias = alias_lookup(raw)

        print(f"ALIAS RESULT: {alias}")

        if alias is UNRESOLVED:
            return FoodMatch(raw, None, 0.0, "unresolved")

        if isinstance(alias, str):
            row = self.db_index.get_by_exact_name(alias)
            if row:
                return FoodMatch(
                    raw,
                    row.get("normalized_name"),
                    1.0,
                    "alias",
                )

        # -----------------------------
        # 2. EXACT MATCH
        # -----------------------------
        row = self.db_index.get_by_exact_name(raw)
        if row:
            return FoodMatch(
                raw,
                row.get("normalized_name"),
                1.0,
                "exact",
            )

        # -----------------------------
        # 3. FUZZY MATCH
        # -----------------------------
        candidates = self.matcher.get_candidates(raw)
        selected = self.selector.select_best(candidates)

        if selected is None:
            return FoodMatch(raw, None, 0.0, "unmatched")

        name, score = selected

        return FoodMatch(
            raw,
            name,
            score / 100.0,
            "fuzzy",
        )