# -*- coding: utf-8 -*-
"""
Example usage of GenParkReasoningBacktrackingCounterfactualAuditor
Demonstrates contradiction detection and automated rollback recommendation.
"""

from client import GenParkReasoningBacktrackingCounterfactualAuditor

def main():
    auditor = GenParkReasoningBacktrackingCounterfactualAuditor()

    flawed_trace = [
        {"step": 0, "content": "Assume there exists a rational number q such that q^2 = 2."},
        {"step": 1, "content": "Write q = a / b in lowest terms where gcd(a, b) = 1."},
        {"step": 2, "content": "Then a^2 = 2 b^2, implying a^2 is even, hence a is even: a = 2k."},
        {"step": 3, "content": "Substitute: 4k^2 = 2b^2 -> b^2 = 2k^2, implying b is even."},
        {"step": 4, "content": "Wait, this contradicts our premise that gcd(a, b) = 1 since both are even."}
    ]

    res = auditor.audit_reasoning_trace(flawed_trace)

    print("================================================================")
    print("GenPark Reasoning Backtracking Auditor - Live Runs")
    print("================================================================\n")
    print(f"Trace Length Steps    : {res['trace_length_steps']} steps")
    print(f"Trace Health Verdict  : {res['trace_health_verdict']}")
    print(f"Contradictions Found  : {res['contradiction_events_count']}")
    print(f"Rollback Checkpoint   : Step #{res['recommended_rollback_step_index']}")
    print(f"Correction Directive  : {res['counterfactual_correction_directive']}\n")

if __name__ == "__main__":
    main()
