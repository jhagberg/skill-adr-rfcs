#!/usr/bin/env python3
"""Grade eval outputs against assertions."""
import json
import re
import os
import sys

BASE = sys.argv[1] if len(sys.argv) > 1 else sys.exit("usage: grade_outputs.py <run-dir>")


def read_file(path):
    with open(path) as f:
        return f.read()


def grade_adr_creation(content, filename):
    results = []
    has_frontmatter = content.startswith("---")
    fm_block = ""
    if has_frontmatter:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_block = parts[1]

    # 1. status in frontmatter
    results.append({
        "text": "Has YAML frontmatter with 'status' field",
        "passed": bool(re.search(r"^status:", fm_block, re.MULTILINE)),
        "evidence": f"Frontmatter block contains 'status:': {'yes' if re.search(r'^status:', fm_block, re.MULTILINE) else 'no'}"
    })
    # 2. date in frontmatter
    results.append({
        "text": "Has YAML frontmatter with 'date' field",
        "passed": bool(re.search(r"^date:", fm_block, re.MULTILINE)),
        "evidence": f"Frontmatter contains 'date:': {'yes' if re.search(r'^date:', fm_block, re.MULTILINE) else 'no'}"
    })
    # 3. decision-makers in frontmatter
    results.append({
        "text": "Has YAML frontmatter with 'decision-makers' field",
        "passed": bool(re.search(r"^decision-makers:", fm_block, re.MULTILINE)),
        "evidence": f"Frontmatter contains 'decision-makers:': {'yes' if re.search(r'^decision-makers:', fm_block, re.MULTILINE) else 'no'}"
    })
    # 4. Context and Problem Statement section
    has_ctx = bool(re.search(r"^##\s+Context and Problem Statement", content, re.MULTILINE))
    results.append({
        "text": "Has 'Context and Problem Statement' section",
        "passed": has_ctx,
        "evidence": f"Section heading found: {has_ctx}"
    })
    # 5. Considered Options with 3+ options
    has_opts = bool(re.search(r"^##\s+Considered Options", content, re.MULTILINE))
    has_pg = "postgresql" in content.lower()
    has_mysql = "mysql" in content.lower()
    has_sqlite = "sqlite" in content.lower()
    all_three = has_pg and has_mysql and has_sqlite
    results.append({
        "text": "Has 'Considered Options' section listing at least 3 options (PostgreSQL, MySQL, SQLite)",
        "passed": has_opts and all_three,
        "evidence": f"Section: {has_opts}, PostgreSQL: {has_pg}, MySQL: {has_mysql}, SQLite: {has_sqlite}"
    })
    # 6. Decision Outcome with quoted option
    has_outcome = bool(re.search(r"^##\s+Decision Outcome", content, re.MULTILINE))
    has_quoted = bool(re.search(r'Chosen option:\s*"', content))
    results.append({
        "text": "Has 'Decision Outcome' section with quoted chosen option name",
        "passed": has_outcome and has_quoted,
        "evidence": f"Section: {has_outcome}, Quoted option: {has_quoted}"
    })
    # 7. Good and Bad consequences
    has_good = bool(re.search(r"\*\s+Good,\s+because", content))
    has_bad = bool(re.search(r"\*\s+Bad,\s+because", content))
    results.append({
        "text": "Has consequences with both 'Good' and 'Bad' items",
        "passed": has_good and has_bad,
        "evidence": f"Good items: {has_good}, Bad items: {has_bad}"
    })
    # 8. Pros and Cons section
    has_proscons = bool(re.search(r"^##\s+Pros and Cons of the Options", content, re.MULTILINE))
    results.append({
        "text": "Has 'Pros and Cons of the Options' section with per-option breakdown",
        "passed": has_proscons,
        "evidence": f"Section found: {has_proscons}"
    })
    # 9. Filename pattern
    fname_ok = bool(re.match(r"^\d{4}-[a-z0-9-]+\.md$", filename))
    results.append({
        "text": "Filename follows NNNN-kebab-case-title.md pattern",
        "passed": fname_ok,
        "evidence": f"Filename '{filename}' matches pattern: {fname_ok}"
    })
    # 10. docs/decisions/ (check if mentioned or implied)
    results.append({
        "text": "Uses docs/decisions/ directory (not docs/adr/)",
        "passed": "docs/adr" not in content.lower(),
        "evidence": "No reference to docs/adr/ in content"
    })
    # 11. template guidance comments must not leak into the final ADR
    leaked = "<!--" in content
    results.append({
        "text": "No template guidance comments (<!-- ... -->) leaked into the ADR",
        "passed": not leaked,
        "evidence": f"HTML comment present in output: {leaked}"
    })
    return results


def grade_rfc_drafting(content, filename):
    results = []
    has_frontmatter = content.startswith("---")
    fm_block = ""
    if has_frontmatter:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_block = parts[1]

    # 1. Is it an RFC?
    is_rfc = bool(re.search(r"(rfc|request for comment)", content.lower()))
    results.append({
        "text": "Correctly produces an RFC (not an ADR) given the cross-team open question",
        "passed": is_rfc,
        "evidence": f"Contains RFC reference: {is_rfc}"
    })
    # 2. YAML frontmatter with status: draft
    has_status_draft = bool(re.search(r"^status:\s*draft", fm_block, re.MULTILINE | re.IGNORECASE))
    results.append({
        "text": "Has RFC-style YAML frontmatter with status set to 'draft'",
        "passed": has_frontmatter and has_status_draft,
        "evidence": f"YAML frontmatter: {has_frontmatter}, status: draft: {has_status_draft}"
    })
    # 3. Summary section
    has_summary = bool(re.search(r"^##\s+Summary", content, re.MULTILINE))
    results.append({
        "text": "Has 'Summary' section",
        "passed": has_summary,
        "evidence": f"Section found: {has_summary}"
    })
    # 4. Motivation section
    has_motivation = bool(re.search(r"^##\s+Motivation", content, re.MULTILINE))
    results.append({
        "text": "Has 'Motivation' section with concrete use cases",
        "passed": has_motivation,
        "evidence": f"Section found: {has_motivation}"
    })
    # 5. Drawbacks section
    has_drawbacks = bool(re.search(r"^##\s+Drawbacks", content, re.MULTILINE))
    results.append({
        "text": "Has 'Drawbacks' section",
        "passed": has_drawbacks,
        "evidence": f"Section found: {has_drawbacks}"
    })
    # 6. Rationale and alternatives covering all 4 options
    has_rationale = bool(re.search(r"^##\s+(Rationale|Options|Alternatives)", content, re.MULTILINE))
    has_auth0 = "auth0" in content.lower()
    has_firebase = "firebase" in content.lower()
    has_keycloak = "keycloak" in content.lower()
    has_custom = bool(re.search(r"custom.*(oauth|provider)|build.*(own|our)", content.lower()))
    all_four = has_auth0 and has_firebase and has_keycloak and has_custom
    results.append({
        "text": "Has 'Rationale and alternatives' section covering all 4 auth options",
        "passed": has_rationale and all_four,
        "evidence": f"Section: {has_rationale}, Auth0: {has_auth0}, Firebase: {has_firebase}, Keycloak: {has_keycloak}, Custom: {has_custom}"
    })
    # 7. Prior art section
    has_prior = bool(re.search(r"^##\s+Prior art", content, re.MULTILINE))
    results.append({
        "text": "Has 'Prior art' section",
        "passed": has_prior,
        "evidence": f"Section found: {has_prior}"
    })
    # 8. Unresolved questions
    has_unresolved = bool(re.search(r"^##\s+Unresolved questions", content, re.MULTILINE))
    results.append({
        "text": "Has 'Unresolved questions' section",
        "passed": has_unresolved,
        "evidence": f"Section found: {has_unresolved}"
    })
    # 9. Outcome section
    has_outcome = bool(re.search(r"^##\s+Outcome", content, re.MULTILINE))
    results.append({
        "text": "Has 'Outcome' section (even if placeholder)",
        "passed": has_outcome,
        "evidence": f"Section found: {has_outcome}"
    })
    # 10. Filename convention
    fname_ok = bool(re.match(r"^\d{4}-[a-z0-9-]+\.md$", filename))
    results.append({
        "text": "Filename follows NNNN-kebab-case-title.md RFC naming convention",
        "passed": fname_ok,
        "evidence": f"Filename '{filename}' matches: {fname_ok}"
    })
    return results


def grade_adr_review(content):
    cl = content.lower()
    results = []

    # 1. Flags brief context
    flags_context = bool(re.search(r"(context.*brief|context.*short|one sentence|too (thin|brief|short)|\"we need caching\".*not)", cl))
    results.append({
        "text": "Flags that context/problem statement is too brief (should be 2-5 sentences)",
        "passed": flags_context,
        "evidence": f"References brief/thin context: {flags_context}"
    })
    # 2. Flags single option
    flags_single = bool(re.search(r"(only one option|single.?option|one option listed|only.*redis|single.*listed|only.*considered)", cl))
    results.append({
        "text": "Flags that only 1 option is considered (needs at least 2 alternatives)",
        "passed": flags_single,
        "evidence": f"References single option: {flags_single}"
    })
    # 3. Flags vague justification
    flags_vague = bool(re.search(r"(it'?s the best.*not|not.*rationale|vague|not.*justif|\"because it'?s the best\")", cl))
    results.append({
        "text": "Flags that justification is vague ('it's the best' is not adequate)",
        "passed": flags_vague,
        "evidence": f"References vague justification: {flags_vague}"
    })
    # 4. Flags missing negative consequences
    flags_neg = bool(re.search(r"(no negative|missing.*negative|only.*positive|no.*bad|only.*good)", cl))
    results.append({
        "text": "Flags missing negative consequences (only 'Good' items present)",
        "passed": flags_neg,
        "evidence": f"References missing negatives: {flags_neg}"
    })
    # 5. Flags missing decision-makers
    flags_dm = bool(re.search(r"(decision.?makers?.*missing|missing.*decision.?makers?|no.*decision.?makers?|decision.?makers?.*not)", cl))
    results.append({
        "text": "Flags missing 'decision-makers' in frontmatter",
        "passed": flags_dm,
        "evidence": f"References missing decision-makers: {flags_dm}"
    })
    # 6. Flags missing Confirmation section
    flags_confirm = bool(re.search(r"(confirmation.*missing|missing.*confirmation|no.*confirmation|validation.*missing|missing.*validation)", cl))
    results.append({
        "text": "Flags missing 'Confirmation' section",
        "passed": flags_confirm,
        "evidence": f"References missing confirmation/validation: {flags_confirm}"
    })
    # 7. Structured review
    has_headers = len(re.findall(r"^##", content, re.MULTILINE)) >= 3
    results.append({
        "text": "Review is structured (not just a wall of text)",
        "passed": has_headers,
        "evidence": f"Has {len(re.findall(r'^##', content, re.MULTILINE))} section headers"
    })
    # 8. Specific improvements
    has_suggestions = bool(re.search(r"(suggest|recommend|replace|rewrite|add|expand|should)", cl))
    results.append({
        "text": "Provides specific improvement suggestions (not just listing problems)",
        "passed": has_suggestions,
        "evidence": f"Contains actionable language: {has_suggestions}"
    })
    return results


def main():
    all_results = {}

    # ADR creation
    for variant in ["with_skill", "without_skill"]:
        d = f"{BASE}/adr-creation-{variant}/outputs"
        files = os.listdir(d)
        md_files = [f for f in files if f.endswith(".md")]
        if md_files:
            fname = md_files[0]
            content = read_file(os.path.join(d, fname))
            results = grade_adr_creation(content, fname)
            key = f"adr-creation-{variant}"
            all_results[key] = results
            passed = sum(1 for r in results if r["passed"])
            print(f"{key}: {passed}/{len(results)}")

    # RFC drafting
    for variant in ["with_skill", "without_skill"]:
        d = f"{BASE}/rfc-drafting-{variant}/outputs"
        files = os.listdir(d)
        md_files = [f for f in files if f.endswith(".md")]
        if md_files:
            fname = md_files[0]
            content = read_file(os.path.join(d, fname))
            results = grade_rfc_drafting(content, fname)
            key = f"rfc-drafting-{variant}"
            all_results[key] = results
            passed = sum(1 for r in results if r["passed"])
            print(f"{key}: {passed}/{len(results)}")

    # ADR review
    for variant in ["with_skill", "without_skill"]:
        path = f"{BASE}/adr-review-{variant}/outputs/review.md"
        content = read_file(path)
        results = grade_adr_review(content)
        key = f"adr-review-{variant}"
        all_results[key] = results
        passed = sum(1 for r in results if r["passed"])
        print(f"{key}: {passed}/{len(results)}")

    # Write grading.json for each
    for key, results in all_results.items():
        # Parse key into dir name
        parts = key.rsplit("-", 1)
        eval_name = parts[0]  # e.g. "adr-creation"
        variant = parts[1]  # "with_skill" or "without_skill"
        # Actually need to reconstruct properly
        if key.startswith("adr-creation"):
            dirname = key.replace("adr-creation-", "adr-creation-")
        elif key.startswith("rfc-drafting"):
            dirname = key.replace("rfc-drafting-", "rfc-drafting-")
        elif key.startswith("adr-review"):
            dirname = key.replace("adr-review-", "adr-review-")
        else:
            dirname = key

        grading_path = f"{BASE}/{dirname}/grading.json"
        passed = sum(1 for r in results if r["passed"])
        total = len(results)
        grading = {
            "eval_id": key,
            "pass_rate": passed / total if total > 0 else 0,
            "passed": passed,
            "total": total,
            "expectations": results
        }
        with open(grading_path, "w") as f:
            json.dump(grading, f, indent=2)

    print("\nAll grading.json files written.")


if __name__ == "__main__":
    main()
