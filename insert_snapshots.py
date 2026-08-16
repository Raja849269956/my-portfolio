import re, io

# Approved text per artifact (no em dashes). Inserted as a callout block after intro <p>.
SNAPSHOT = {
"artifact-1.html": """<div class="callout">
<div class="label" style="margin-bottom:.5rem">Artifact Snapshot</div>
<p><strong>Objective:</strong> Demonstrate the ability to design and ship a production-grade, no-code AI assistant using Chatbase and GPT-4o-mini that delivers structured behavioral interview feedback through prompt engineering, constraint design, and adversarial testing.</p>
<p><strong>Unique value:</strong> Built from a real enterprise automation mindset with input, output, and feedback contracts, hard-blocked illegal-question constraints, and 15-scenario adversarial testing at a 93% pass rate that mirrors how I validate bots at BNY.</p>
<p><strong>Relevance:</strong> Shows hiring managers and AI/ML leads that I can take an AI idea from design to tested deployment instead of stopping at a prototype.</p>
<p><strong>References:</strong> AI tools used include Chatbase for the chatbot platform, OpenAI GPT-4o-mini for generation, and prompt-engineering iteration. All decisions and evaluation are my own.</p>
</div>""",

"artifact-2.html": """<div class="callout">
<div class="label" style="margin-bottom:.5rem">Artifact Snapshot</div>
<p><strong>Objective:</strong> Demonstrate model-selection reasoning by comparing ML and DL on two real cases, banking fraud detection and autonomous-driving image recognition, and justifying the right method for each problem.</p>
<p><strong>Unique value:</strong> Uses my banking and fraud-monitoring domain knowledge to show why explainability and data structure drive the choice more than model sophistication.</p>
<p><strong>Relevance:</strong> Shows I can communicate technical trade-offs to risk, business, and engineering stakeholders.</p>
<p><strong>References:</strong> AI tools used include GPT-4o-mini for drafting and revision support, with case examples drawn from industry practice. Analysis and conclusions are my own.</p>
</div>""",

"artifact-3.html": """<div class="callout">
<div class="label" style="margin-bottom:.5rem">Artifact Snapshot</div>
<p><strong>Objective:</strong> Demonstrate the ability to explain a technical ML concept, how neural networks learn, to a non-technical audience through disciplined iterated prompt work.</p>
<p><strong>Unique value:</strong> The Einstein challenge framing plus a documented iteration log showing how feedback refined the explanation, a communication skill that is rare in technical portfolios.</p>
<p><strong>Relevance:</strong> Shows I can make AI understandable to stakeholders, which is a core professional competency.</p>
<p><strong>References:</strong> AI tools used include generative AI, GPT-4o-mini, for drafting, with iterative refinement guided by my own feedback. The final explanation is my own.</p>
</div>""",

"artifact-4.html": """<div class="callout">
<div class="label" style="margin-bottom:.5rem">Artifact Snapshot</div>
<p><strong>Objective:</strong> Demonstrate operational ML competency in handling messy data, class imbalance, privacy, bias, and post-deployment monitoring in production.</p>
<p><strong>Unique value:</strong> Grounded in my BNY mainframe, QA, and automation experience with bot-failure imbalance, override logging, and regulated-data handling, which turns theory into enterprise practice.</p>
<p><strong>Relevance:</strong> Shows ML engineering leads and risk partners that I understand reliability and not just accuracy.</p>
<p><strong>References:</strong> AI tools used include the SchoolAI Data Challenge Coach for the scenario walkthrough and GPT-4o-mini for revision. Decisions and the write-up are my own.</p>
</div>""",
}

for fn, block in SNAPSHOT.items():
    h = open(fn, encoding='utf-8').read()
    # insert right after the first intro <p> that follows the <h1> title
    # find <h1>...</h1> then the next <p>...</p>, insert after it
    m = re.search(r'(<h1[^>]*>.*?</h1>\s*<p>.*?</p>)', h, re.S)
    if not m:
        print("NO MATCH in", fn); continue
    insert_at = m.end()
    if "Artifact Snapshot" in h:
        print("ALREADY HAS SNAPSHOT in", fn); continue
    new = h[:insert_at] + "\n" + block + "\n" + h[insert_at:]
    open(fn, "w", encoding='utf-8').write(new)
    print("INSERTED snapshot into", fn, "| size", len(new))
