#!/usr/bin/env python3
"""
Upgrade structured data (Schema.org) and embed matching sample practice problems
across all 48 CBSE Class 10 chapter test pages on MockTestVault.

Generates unified 2026-compliant @graph JSON-LD:
1. BreadcrumbList (exact hierarchical navigation)
2. Quiz (rich learningResourceType, assesses, educationalAlignment, isAccessibleForFree, offers, and hasPart Question/Answer objects)
3. LearningResource (study module metadata, teaches, assesses, timeRequired)

Also injects corresponding visible Sample Examination Problems & Official Solutions
into each page's <section class="cbt-academic-guide">, achieving 100% compliance with
Google Search Central's Content Visibility and Rich Snippets standards.
"""

import os
import sys
import json
import re
import html
from pathlib import Path

# Add script directory to path
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.append(str(SCRIPT_DIR))

from generate_class10_guides import CHAPTER_GUIDES

ROOT_DIR = Path("/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com")
CBSE10_DIR = ROOT_DIR / "cbse-class-10"

LETTERS = ["A", "B", "C", "D"]

def clean_concept_name(name: str) -> str:
    # Strip leading emoji and whitespace
    return re.sub(r'^[^\w\s]+\s*', '', name).strip()

def process_chapter(rel_path: str, guide: dict) -> bool:
    html_path = CBSE10_DIR / rel_path
    if not html_path.exists():
        print(f"Error: {html_path} does not exist.")
        return False

    content = html_path.read_text(encoding="utf-8")

    # 1. Extract Set 1 path
    m_set1 = re.search(r'set1:\s*[\'"]([^\'"]+)[\'"]', content)
    if not m_set1:
        print(f"Error: set1 not found in {rel_path}")
        return False

    set1_rel = m_set1.group(1)
    set1_full = (html_path.parent / set1_rel).resolve()
    if not set1_full.exists():
        print(f"Error: set1 file {set1_full} not found")
        return False

    with open(set1_full, "r", encoding="utf-8") as f:
        q_data = json.load(f)
    questions = q_data.get("questions", []) if isinstance(q_data, dict) else q_data
    if len(questions) < 2:
        print(f"Error: fewer than 2 questions in {set1_full}")
        return False

    sample_qs = questions[:2]

    # 2. Extract existing Breadcrumbs from Tag 2
    m_bc = re.search(
        r'<script type="application/ld\+json">\s*(\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"BreadcrumbList".*?\})\s*</script>',
        content,
        re.DOTALL
    )
    if not m_bc:
        print(f"Error: BreadcrumbList tag not found in {rel_path}")
        return False

    bc_json = json.loads(m_bc.group(1))
    breadcrumbs = bc_json.get("itemListElement", [])

    canonical_url = f"https://mocktestvault.com/cbse-class-10/{rel_path}"

    # 3. Construct hasPart for Quiz
    has_part = []
    for q in sample_qs:
        ans_idx = q["answer"]
        correct_text = q["options"][ans_idx]
        suggested = []
        for idx, opt in enumerate(q["options"]):
            suggested.append({
                "@type": "Answer",
                "position": idx,
                "text": opt
            })

        has_part.append({
            "@type": "Question",
            "name": q["question"],
            "eduQuestionType": "Multiple choice",
            "learningResourceType": "Practice problem",
            "suggestedAnswer": suggested,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": correct_text,
                "comment": {
                    "@type": "Comment",
                    "text": q["explanation"]
                }
            }
        })

    # Concept pillars
    concepts = [clean_concept_name(card[0]) for card in guide["cards"]]

    # 4. Construct unified @graph Schema.org JSON-LD
    schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
                "itemListElement": breadcrumbs
            },
            {
                "@type": "Quiz",
                "@id": f"{canonical_url}#quiz",
                "url": canonical_url,
                "name": f"CBSE Class 10 {guide['subject']} {guide['title']} MCQ Practice Test",
                "description": f"Official CBSE Class 10 Board exam practice test for {guide['title']} with timer, negative marking options, and step-by-step NCERT solutions.",
                "educationalLevel": "Grade 10",
                "learningResourceType": "Practice Quiz",
                "educationalUse": "Assessment",
                "inLanguage": "en",
                "isAccessibleForFree": True,
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "INR",
                    "availability": "https://schema.org/InStock"
                },
                "provider": {
                    "@type": "Organization",
                    "name": "MockTestVault",
                    "url": "https://mocktestvault.com"
                },
                "about": {
                    "@type": "Thing",
                    "name": guide["title"]
                },
                "educationalAlignment": [
                    {
                        "@type": "AlignmentObject",
                        "alignmentType": "educationalSubject",
                        "targetName": guide["subject"]
                    },
                    {
                        "@type": "AlignmentObject",
                        "alignmentType": "educationalLevel",
                        "targetName": "Class 10"
                    },
                    {
                        "@type": "AlignmentObject",
                        "alignmentType": "academicFramework",
                        "targetName": "Central Board of Secondary Education (CBSE)"
                    }
                ],
                "assesses": concepts,
                "hasPart": has_part
            },
            {
                "@type": "LearningResource",
                "@id": f"{canonical_url}#learningresource",
                "url": canonical_url,
                "name": f"CBSE Class 10 {guide['subject']} {guide['title']} Blueprint & Study Guide",
                "description": guide["overview"],
                "educationalLevel": "Class 10",
                "learningResourceType": "Study Guide",
                "educationalUse": ["practice", "assessment", "study-guide"],
                "inLanguage": "en",
                "isAccessibleForFree": True,
                "timeRequired": "PT45M",
                "teaches": concepts,
                "assesses": concepts,
                "provider": {
                    "@type": "Organization",
                    "name": "MockTestVault",
                    "url": "https://mocktestvault.com"
                }
            }
        ]
    }

    graph_json_str = json.dumps(schema_graph, indent=2, ensure_ascii=False)
    new_schema_tag = f'  <!-- Schema.org Unified 2026 Structured Data (@graph: BreadcrumbList, Quiz with Practice Problems, LearningResource) -->\n  <script type="application/ld+json">\n{graph_json_str}\n  </script>'

    # 5. Replace Schema Tags in <head>
    # Match first tag (Quiz)
    quiz_pattern = re.compile(r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"Quiz".*?</script>', re.DOTALL)
    if not quiz_pattern.search(content):
        print(f"Error: Quiz script tag pattern did not match in {rel_path}")
        return False
    content = quiz_pattern.sub(new_schema_tag, content, count=1)

    # Remove second tag (BreadcrumbList) and preceding comment if present
    bc_remove_pattern = re.compile(r'\s*(?:<!--\s*Schema\.org BreadcrumbList Structured Data\s*-->\s*)?<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"BreadcrumbList".*?</script>', re.DOTALL)
    content = bc_remove_pattern.sub('', content, count=1)

    # 6. Format Visible Sample Problems HTML
    problems_html = '\n    <!-- Sample Board Practice Problems & Marking Key (Structured Data & Wave-1 SEO Alignment) -->\n'
    problems_html += '    <div style="background:var(--bg-surface); border:1px solid var(--border-color); border-radius:8px; padding:20px; margin-bottom:24px;">\n'
    problems_html += '      <h3 style="font-size:1.05rem; font-weight:700; color:var(--text-primary); margin-bottom:14px; display:flex; align-items:center; gap:8px;">\n'
    problems_html += '        <span>📝 Sample Board Examination Problems &amp; Official Solutions</span>\n'
    problems_html += '      </h3>\n'

    for idx, q in enumerate(sample_qs):
        subtopic = html.escape(q.get("subtopic", "Concept Check"))
        q_text = html.escape(q["question"])
        border_style = 'margin-bottom:16px; padding-bottom:16px; border-bottom:1px dashed var(--border-color);' if idx == 0 else ''

        opts_li = ""
        for o_idx, opt in enumerate(q["options"]):
            opts_li += f'          <li><strong>({LETTERS[o_idx]})</strong> {html.escape(opt)}</li>\n'

        ans_idx = q["answer"]
        ans_letter = LETTERS[ans_idx]
        correct_text = html.escape(q["options"][ans_idx])
        explanation = html.escape(q["explanation"])
        citation = html.escape(q.get("citation", ""))
        citation_html = f'<p style="margin:4px 0 0; font-size:0.75rem; color:var(--text-muted);"><strong>NCERT Source:</strong> {citation}</p>' if citation else ''

        problems_html += f'''      <div style="{border_style}">
        <p style="font-size:0.9rem; font-weight:600; color:var(--text-primary); margin-bottom:10px;">
          <strong>Q{idx+1} ({subtopic}):</strong> {q_text}
        </p>
        <ul style="margin:0 0 10px 20px; padding:0; font-size:0.85rem; color:var(--text-secondary); line-height:1.6;">
{opts_li}        </ul>
        <details style="background:var(--bg-subtle); border-radius:6px; padding:8px 12px; font-size:0.82rem; cursor:pointer;">
          <summary style="font-weight:600; color:var(--primary);">
            🔍 View Correct Answer &amp; Step-by-Step Marking Explanation
          </summary>
          <div style="margin-top:8px; color:var(--text-secondary); line-height:1.5;">
            <p style="margin-bottom:4px;"><strong style="color:var(--text-primary);">Correct Answer:</strong> Option ({ans_letter}) — {correct_text}</p>
            <p style="margin:0;"><strong>Explanation:</strong> {explanation}</p>
            {citation_html}
          </div>
        </details>
      </div>\n'''

    problems_html += '    </div>\n'

    # Check if sample problems were already injected
    if 'Sample Board Examination Problems &amp; Official Solutions' in content:
        # Replace existing sample problems block
        content = re.sub(
            r'\s*<!-- Sample Board Practice Problems & Marking Key.*?</div>\s*</div>\n',
            problems_html,
            content,
            flags=re.DOTALL
        )
    else:
        # Inject right above the marking scheme block
        target = '<div style="background:var(--bg-subtle); border-radius:8px; padding:18px; margin-bottom:24px; font-size:0.88rem;'
        if target not in content:
            print(f"Error: Marking scheme target not found in {rel_path}")
            return False
        content = content.replace(target, problems_html + '\n    ' + target, 1)

    # 7. Write updated file
    html_path.write_text(content, encoding="utf-8")
    return True

def main():
    print("=" * 65)
    print("⚡ Upgrading Schema.org & Sample Problems across 48 CBSE Class 10 Pages")
    print("=" * 65)

    success_count = 0
    for rel_path, guide in CHAPTER_GUIDES.items():
        ok = process_chapter(rel_path, guide)
        if ok:
            success_count += 1
            print(f"✓ [{success_count}/48] Upgraded {rel_path}")
        else:
            print(f"✗ Failed {rel_path}")

    print("=" * 65)
    print(f"🎉 Complete! Successfully upgraded {success_count}/48 chapter pages.")
    print("=" * 65)

if __name__ == "__main__":
    main()
