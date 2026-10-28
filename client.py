# -*- coding: utf-8 -*-
"""
GenPark Reasoning Backtracking Counterfactual Auditor Client
Detects reasoning loops, deadlocks, and logical contradictions to execute non-destructive checkpoint rollbacks.
Zero external dependencies -- Python 3.9+ standard library only.
"""

import math
import hashlib
import re
from typing import Dict, Any, List

class GenParkReasoningBacktrackingCounterfactualAuditor:
    """
    Monitors sequential thought steps in deliberate System 2 reasoning trajectories.
    Identifies repeated cyclical statements, contradiction traps, and calculates
    the optimal ancestor checkpoint to rollback and restart exploration.
    """

    def __init__(self, loop_similarity_threshold: float = 0.85):
        self.loop_thresh = loop_similarity_threshold

    def compute_statement_fingerprint(self, text: str) -> str:
        """Normalized bag-of-words hash for fast loop detection."""
        words = sorted(set(re.sub(r'[^a-zA-Z0-9]', '', w.lower()) for w in text.split()))
        return hashlib.md5(" ".join(words).encode()).hexdigest()

    def audit_reasoning_trace(
        self,
        reasoning_trace_steps: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Audits full thought trace for cycles, contradictions, and dead ends.
        """
        if not reasoning_trace_steps:
            return {"error": "Empty trace"}

        seen_fingerprints = {}
        contradiction_flags = []
        cycle_detected = False
        loop_indices = []

        for idx, step in enumerate(reasoning_trace_steps):
            text = step.get("content", "")
            fp = self.compute_statement_fingerprint(text)

            # Cycle detection
            if fp in seen_fingerprints:
                prior_idx = seen_fingerprints[fp]
                cycle_detected = True
                loop_indices.append((prior_idx, idx))
            else:
                seen_fingerprints[fp] = idx

            # Contradiction heuristic: step asserts negation of an established assumption
            lower = text.lower()
            if "wait, this contradicts" in lower or "this is impossible" in lower or "contradiction arises" in lower:
                contradiction_flags.append({
                    "step_index": idx,
                    "evidence_text": text,
                    "contradiction_type": "EXPLICIT_MODEL_CONTRADICTION"
                })

        # Calculate optimal rollback checkpoint
        rollback_target = None
        if contradiction_flags:
            # Rollback to 1 step before the earliest premise that caused the contradiction
            culprit_idx = contradiction_flags[0]["step_index"]
            rollback_target = max(0, culprit_idx - 2)
            directive = f"Rollback to checkpoint Step #{rollback_target}. Invalidate previous branch assumption."
        elif cycle_detected:
            start_loop, end_loop = loop_indices[0]
            rollback_target = max(0, start_loop - 1)
            directive = f"Cycle detected between Step #{start_loop} and Step #{end_loop}. Rollback to Step #{rollback_target} and branch counterfactually."
        else:
            directive = "Trace is monotonic, coherent, and free of cyclical deadlocks."

        is_healthy = not (cycle_detected or contradiction_flags)

        return {
            "trace_length_steps": len(reasoning_trace_steps),
            "trace_health_verdict": "HEALTHY_MONOTONIC" if is_healthy else ("CONTRADICTION_DEADLOCK" if contradiction_flags else "CIRCULAR_REASONING_LOOP"),
            "cycle_detected": cycle_detected,
            "contradiction_events_count": len(contradiction_flags),
            "detected_loops": loop_indices,
            "flagged_contradictions": contradiction_flags,
            "recommended_rollback_step_index": rollback_target,
            "counterfactual_correction_directive": directive
        }
