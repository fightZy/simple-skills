from __future__ import annotations


def score_retrieval(
    *,
    expected_candidate_ids: list[str] | tuple[str, ...],
    actual_candidate_ids: list[str] | tuple[str, ...],
    actual_layers: list[str] | tuple[str, ...],
    expected_layers: list[str] | tuple[str, ...] = (),
    expected_top_id: str | None = None,
    forbidden_candidate_ids: list[str] | tuple[str, ...] = (),
) -> dict[str, object]:
    expected = list(expected_candidate_ids)
    actual = list(actual_candidate_ids)
    actual_layer_list = list(actual_layers)
    expected_layer_list = list(expected_layers)
    forbidden = list(forbidden_candidate_ids)

    reciprocal_rank = 0.0
    for index, candidate_id in enumerate(actual, start=1):
        if candidate_id in expected:
            reciprocal_rank = 1.0 / index
            break

    def recall_at(k: int) -> float:
        if not expected:
            return 1.0 if not actual[:k] else 0.0
        hits = [candidate_id for candidate_id in actual[:k] if candidate_id in expected]
        return 1.0 if hits else 0.0

    layer_hit = True
    if expected_layer_list:
        layer_hit = any(layer in expected_layer_list for layer in actual_layer_list)

    false_positive = not expected and bool(actual)
    forbidden_hit = any(candidate_id in forbidden for candidate_id in actual)
    expected_top_hit = matches_expected_top_id(
        expected_top_id=expected_top_id,
        actual_candidate_ids=actual,
        actual_layers=actual_layer_list,
    )

    return {
        "recall_at_1": recall_at(1),
        "recall_at_3": recall_at(3),
        "recall_at_5": recall_at(5),
        "mrr": reciprocal_rank,
        "top_hit": bool(actual and expected and actual[0] in expected),
        "expected_top_hit": expected_top_hit,
        "layer_hit": layer_hit,
        "false_positive": false_positive,
        "forbidden_hit": forbidden_hit,
        "expected_count": len(expected),
        "retrieved_count": len(actual),
    }


def matches_expected_top_id(
    *,
    expected_top_id: str | None,
    actual_candidate_ids: list[str],
    actual_layers: list[str],
) -> bool:
    if expected_top_id is None:
        return True
    if not actual_candidate_ids:
        return False
    if is_base_candidate(expected_top_id, ""):
        return actual_candidate_ids[0] == expected_top_id

    for candidate_id, layer in zip(actual_candidate_ids, actual_layers):
        if is_base_candidate(candidate_id, layer):
            continue
        return candidate_id == expected_top_id
    return False


def is_base_candidate(candidate_id: str, layer: str) -> bool:
    return layer in {"generated-index", "generated-summary"} or candidate_id.startswith(
        ("generated-index:", "generated-summary:")
    )
