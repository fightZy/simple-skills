from __future__ import annotations

import re


def normalize_answer(text: str) -> str:
    collapsed = re.sub(r"\s+", " ", text.strip().lower())
    return collapsed


def run_qa_case(
    *,
    case_gold_answer: str | None,
    question: str,
    retrieved_context: list[str],
    adapter: object | None,
    model_config: dict[str, str] | None,
) -> dict[str, object]:
    if not model_config:
        return {"status": "skipped", "reason": "model configuration missing"}
    if adapter is None:
        return {"status": "skipped", "reason": "adapter missing"}

    response = adapter.answer(
        question=question,
        retrieved_context=retrieved_context,
        model_config=model_config,
    )
    answer = str(response.get("answer", ""))
    result: dict[str, object] = {
        "status": "answered",
        "answer": answer,
        "latency_ms": response.get("latency_ms"),
    }
    if case_gold_answer is not None:
        result["is_correct"] = normalize_answer(answer) == normalize_answer(case_gold_answer)
    return result
