<div align="center">

# LydiaHub

<picture>
  <source media="(max-width: 600px)" srcset="assets/hero-mobile.svg">
  <img src="assets/hero.svg" alt="LydiaHub · Browser Agent Blueprint and CoverCalc Pro" width="100%">
</picture>

> **I turn those “there must be a clearer way” moments into small tools people can try.**
>
> Right now: a reproducible browser-agent recovery demo and a garden-material calculator that checks bags, bulk minimums, and delivery together.

[Open the Blueprint demo guide](https://lydiatools.github.io/browser-agent-blueprint/) · [Try CoverCalc Pro](https://covercalcpro.com/?utm_source=github&utm_medium=referral&utm_campaign=lydiatools_profile#calculator) · [Explore the other tools](#choose-by-the-problem)

Team products I contribute to: [BFTOOLS](https://github.com/mercedesbestsupplier-maker#products)

</div>

---

## Start here · Two projects you can try

### Browser Agent Blueprint · Check what happened before trying again

**Save timed out. Did the record go through?** The blueprint separates attempted actions from verified outcomes so a resumed run checks the page before retrying. The [project demo guide](https://lydiatools.github.io/browser-agent-blueprint/) explains the browser-only test fixture and the full local recovery runner. The browser-only fixture lets you save once, reload, and read back the saved count; it is a test page, not an agent demo. The local recovery runner uses two separate processes and finishes with one saved record. The repository includes 12 original plain-text prompt modules, 4 workflow templates, and 6 reproducible scenarios.

<a href="https://github.com/LydiaTools/browser-agent-blueprint#quick-start"><img src="assets/browser-agent-recovery.png" alt="Browser Agent Blueprint recovery evidence: two separate processes, one saved record, and a DONE checkpoint after readback" width="720"></a>

*Two separate processes; one saved record after resume. Actual synthetic-fixture capture and recorded run output, with an explanatory layout.*

The demo uses deterministic host code and makes no model calls. Muse, Grok, and Codex integration contracts are provided but have not been live-tested. Automatic wake-up and production crash consistency need host support.

**[Project overview and demo guide](https://lydiatools.github.io/browser-agent-blueprint/)** · [Modules and full recovery demo](https://github.com/LydiaTools/browser-agent-blueprint#quick-start) · [Report a synthetic failure case](https://github.com/LydiaTools/browser-agent-blueprint/issues)

### CoverCalc Pro · Check the quantities before placing an order

**From volume to an actual buying decision.** Whole bags, bulk minimums, order increments, and delivery fees are calculated together. In the website's worked example, a 2 yd³ supplier minimum changes the bulk order: 14 bags cost USD 80 delivered, while bulk costs USD 105.

<a href="https://covercalcpro.com/?utm_source=github&utm_medium=referral&utm_campaign=lydiatools_profile#calculator"><picture><source media="(max-width: 600px)" srcset="assets/covercalc-cost-mobile.png"><img src="assets/covercalc-cost-comparison.png" alt="Real CoverCalc Pro result: 14 whole bags cost USD 80 including delivery; the 2-cubic-yard minimum bulk order costs USD 105" width="720"></picture></a>

*Real calculator output using the site's example inputs: 100 ft² at 3 in, 10% allowance, a 2 yd³ bulk minimum, and illustrative prices.*

<details>
<summary>See the measurements, allowance, and supplier rules behind that result</summary>

<img src="assets/covercalc-pro-live.png" alt="The measured 0.926 cubic yards becomes 14 whole bags or a 2-cubic-yard bulk minimum in CoverCalc Pro" width="720">

</details>

Measured length, width, and depth tell you how much space to fill. The volume printed on a bag tells you how many bags to buy. This toolkit keeps the two calculations separate. Check rectangular or circular spaces and inspect the formulas, field definitions, and coverage CSV.

The single-area checker runs on GitHub Pages or as an HTML file you can open offline, without an account or third-party dependencies. The full live calculator is at covercalcpro.com. Repository examples don't guess prices, densities, or supplier rules.

**[Try the open-source checker](https://lydiatools.github.io/covercalcpro-landscape-quantity-kit/tools/landscape-volume-check.html)** · **[Open the full live calculator](https://covercalcpro.com/?utm_source=github&utm_medium=referral&utm_campaign=lydiatools_profile#calculator)** · **[Download the offline checker](https://github.com/LydiaTools/covercalcpro-landscape-quantity-kit/releases/download/v0.1.1/CoverCalcPro-Landscape-Volume-Check-v0.1.1.zip)** · [Toolkit and source](https://github.com/LydiaTools/covercalcpro-landscape-quantity-kit) · [Try the example](https://github.com/LydiaTools/covercalcpro-landscape-quantity-kit/blob/main/docs/TRY-IT.md)

---

## Choose by the problem

New creator tools: **[Xiaohongshu NoteSignal · 小红书笔记风向标](https://github.com/LydiaTools/notesignal)** and **[Global Longform SEO Studio · 海外长文 SEO 量产](https://github.com/LydiaTools/longform-atlas)**. Their working screens and download links are directly below the table.

| What is getting in your way? | Tool | What it helps you do | Current status |
| --- | --- | --- | --- |
| A browser agent times out, loses its place, or submits twice, and you can't tell what happened | [Browser Agent Blueprint](https://github.com/LydiaTools/browser-agent-blueprint) | Reuse prompt modules and run a real local browser against a synthetic page to inspect checkpoints, risk gates, and resume boundaries | MIT; [project demo guide](https://lydiatools.github.io/browser-agent-blueprint/), and local recovery runner; model integrations not tested |
| You want to check dimensions, volume, and bag counts before buying landscape materials | [CoverCalc Pro toolkit](https://github.com/LydiaTools/covercalcpro-landscape-quantity-kit) | Check rectangular or circular volumes, formulas, pack sizes, and shopping quantities | MIT; [live open-source checker](https://lydiatools.github.io/covercalcpro-landscape-quantity-kit/tools/landscape-volume-check.html) / [offline HTML v0.1.1](https://github.com/LydiaTools/covercalcpro-landscape-quantity-kit/releases/tag/v0.1.1) / [full calculator](https://covercalcpro.com/?utm_source=github&utm_medium=referral&utm_campaign=lydiatools_profile#calculator) |
| One useful idea needs four platform images, but reusing one crop loses the point | [Aspectory](https://github.com/LydiaTools/aspectory) | Compose Pinterest, Instagram, Lemon8, and Facebook images from the same verified insight; pick a visual style and export four native PNGs in one ZIP | MIT; [live studio](https://lydiatools.github.io/aspectory/); local image composition, no automatic posting |
| You need source-linked Xiaohongshu examples for your own content research | [Xiaohongshu NoteSignal](https://github.com/LydiaTools/notesignal) | Review visible notes in a bilingual Chrome extension; optional bounded visible-browser collection saves a small sample for later checking | MIT; [v0.1.1 early preview](https://github.com/LydiaTools/notesignal/releases/tag/v0.1.1); live signed-in capture not yet accepted |
| You have keywords but need a creator identity and a repeatable overseas article pipeline | [Global Longform SEO Studio](https://github.com/LydiaTools/longform-atlas) | Define your IP, build distinct evidence-led plans for X Articles, Quora, Medium, LinkedIn or Substack, then draft and export in English or Chinese | MIT; [v0.2.0 local download](https://github.com/LydiaTools/longform-atlas/releases/tag/v0.2.0); offline plan/outline works without an API |
| You understand every word of a long message, but still don't know what you're being asked to do | [Say It Plainly](https://github.com/LydiaTools/shuorenhua/blob/main/README.en.md) | Identify actions and questions, then draft a reply that reflects what you actually mean | macOS v0.9.0; download available; Chinese interface |
| A client's “small change” keeps growing, and nobody can say how much extra work it adds | [Scope Check](products/biefangong/README.md) | Compare a new request with the agreed scope; spot additions, changes, and unanswered questions | macOS v0.1.0; private testing; Chinese interface |
| Ideas and tasks disappear while you switch between apps | [Desktop Flow](https://afdian.com/album/1f24622aa83511f184a452540025c377) | Catch them on your desktop, save as Markdown, and connect to Obsidian or Codex when useful | macOS v1.0.0; Windows v1.0.3 |
| You spend hours in Codex and want a workspace that feels more like yours | [Codex Skin Workshop](https://afdian.com/album/26288eaca83511f19cc352540025c377) | Search, preview, install, switch, and restore skins | macOS; free access; original app by [@luhaozwork](https://github.com/luhaozwork), my enhancements and skins |
| Every new content topic sends you back through the same research and sorting steps | [Xiaoran Topic Assistant](https://afdian.com/a/lydiahub2026) | Put repeated research steps into a workflow, leaving the judgment to you | Released; see the access page |
| Inquiries sit in a spreadsheet, with no clear priority or next step | [Lydia Foreign Trade System](https://github.com/LydiaTools/lydia-foreign-trade-system) | Import CSV or JSON; review grades, missing evidence, and next actions before confirming follow-up | MIT; local setup with Node.js 20+ |

New here? Open the [getting-started page](GETTING-STARTED.md). Pick the problem you recognize and try one tool.

### Xiaohongshu NoteSignal · Turn visible notes into source-linked observations

Capture a note you can see, correct the extracted fields, add your own judgment, and compare saved examples. The optional visible-browser runner collects a small bounded sample into JSON for review; it stops at verification or account warnings.

<a href="https://github.com/LydiaTools/notesignal"><img src="assets/notesignal-popup-empty.png" alt="Xiaohongshu NoteSignal's actual bilingual Chrome extension popup in its empty state, showing manual note capture and visible-result review" width="360"></a>

*Actual popup interface with an empty local library. Live signed-in Xiaohongshu capture is not yet accepted; this screenshot does not show collected content.*

**[Source and setup](https://github.com/LydiaTools/notesignal)** · [Early-preview ZIP](https://github.com/LydiaTools/notesignal/releases/tag/v0.1.1)

### Global Longform SEO Studio · Build a creator IP and its article pipeline

Enter keywords and an audience to suggest a creator positioning, or write your own. Turn that IP into distinct article plans for X Articles, Quora Answers, Medium, LinkedIn Articles, and Substack. Add article-specific evidence, then create an offline outline or draft up to three pieces with your own compatible model. Edit and export Markdown.

<a href="https://github.com/LydiaTools/longform-atlas"><img src="assets/longform-atlas-ip-plan.png" alt="Actual Longform Atlas local article plan: CoverCalc Pro creator positioning with different X Articles, Quora, and Medium angles and separate evidence fields" width="720"></a>

*Actual local app using its built-in gardening sample and offline article plan. No model-generated article, publication result, ranking, or revenue is represented.*

**[Source and quick start](https://github.com/LydiaTools/longform-atlas)** · [v0.2.0 ZIP](https://github.com/LydiaTools/longform-atlas/releases/tag/v0.2.0)

---

## Two more tools I keep improving

### Say It Plainly · Understand the message, then reply in your own words

“Find a lever for user value and close the loop quickly.” You know the words. The hard part is figuring out what to do first, how far to take it, and how to reply without pretending the request was clear.

Say It Plainly breaks a message into actions and the questions worth checking, then drafts a reply around what you actually mean. It checks for added promises about timing, scope, responsibility, or guarantees. The draft goes back into your chat input; you review it before sending.

**One message, two decisions.** First identify the actions and the missing meeting time. Then write a reply from the user's stated intent and check its timing, scope, and responsibility.

<p><img src="assets/say-it-plainly-v0.9.0.png" alt="Actual Say It Plainly output: three action items and a question about the meeting time" width="320"> <img src="assets/say-it-plainly-reply.png" alt="Actual Say It Plainly reply preserves the user's tomorrow-morning delivery intention and asks for the meeting time; intent check is shown" width="320"></p>

*v0.9.0, Chinese interface. Real generated results from a fictional work message; the reply remained unsent.*

**[Product and v0.9.0 downloads](https://github.com/LydiaTools/shuorenhua)** · [English overview](https://github.com/LydiaTools/shuorenhua/blob/main/README.en.md)

### Scope Check · Make the extra work clear before doing it

To a client, it may be “just add a mobile version.” For the person doing the work, it can change the pages, APIs, tests, and delivery date together.

Scope Check keeps the agreement currently confirmed for each project. Paste a new client message and it highlights additions, changes to the agreement, and details that need clarification before work starts. It also drafts a calm confirmation reply that doesn't commit you in advance.

<img src="assets/biefangong-v0.1.0.png" alt="Scope Check identifies mobile adaptation and data export as additions to the saved agreement, asks about the unchanged deadline, and drafts a confirmation reply" width="440">

*v0.1.0, Chinese interface. Fictional scope-change example; the saved agreement is the comparison baseline.*

**[Features and testing status](products/biefangong/README.md)**

---

## Open-source projects · See the code and try it yourself

### Lydia Foreign Trade System · Sort the inquiries before deciding who to follow up with

Start with an inquiry sheet you already have. Check the columns before importing, then review A / B / C / D / HOLD grades, missing evidence, and next actions. When evidence is missing, look up public company information as needed. Keep customer groups separate and export important batches as complete backups.

The interface and screenshots use fictional examples, not actual customers or sales results. It runs locally by default and does not send bulk messages. Local data is not encrypted; the project explains its use boundaries.

<a href="https://github.com/LydiaTools/lydia-foreign-trade-system"><img src="assets/foreign-trade-demo.png" alt="Lydia Foreign Trade System: example companies graded B, C, D, and HOLD, with missing evidence and next actions" width="680"></a>

*Chinese interface, fictional demo inquiries.*

**[Project and real screenshots](https://github.com/LydiaTools/lydia-foreign-trade-system)** · [English getting started](https://github.com/LydiaTools/lydia-foreign-trade-system/blob/main/docs/README.en.md) · [Report an issue](https://github.com/LydiaTools/lydia-foreign-trade-system/issues)

---

## More tools and ideas

### Desktop Flow · Catch the thought before switching apps

Keep a fleeting task or idea on your desktop, then move it into Obsidian, Codex, or a review workflow when useful.

<a href="https://afdian.com/album/1f24622aa83511f184a452540025c377"><img src="assets/desktop-flow-capture-proof.png" alt="Desktop Flow evidence: the captured demo task appears in the application and the same task is read back from the created Markdown file" width="720"></a>

*macOS v1.0.0. Actual app capture and Markdown readback; an explanatory layout. Optional Codex review was not run for this capture.*

### Codex Skin Workshop · Make the daily workspace yours

Make a daily workspace more comfortable, with a way to restore the original appearance. [@luhaozwork](https://github.com/luhaozwork) developed the original app; I contribute feature enhancements and a collection of several hundred skins.

<a href="https://github.com/mercedesbestsupplier-maker/bifang-codex-skins"><img src="assets/skin-workshop-library.png" alt="Actual Skin Workshop manager: searchable preview library, import controls, and apply-and-verify buttons" width="720"></a>

*The manager shows 151 skins in this installed build, searchable previews, and an apply-and-verify control. Original application by @luhaozwork; my contributions are the enhancements and skin collection.*

### Xiaoran Topic Assistant · Turn a brief into topics you can develop

Put repeated research and topic-sorting steps into a workflow, leaving the judgment to you.

<a href="https://afdian.com/a/lydiahub2026"><img src="assets/xiaoran-output-excerpt.svg" alt="Translated excerpt from Xiaoran's recorded sample: a topic proposal connects the audience's problem to a useful deliverable and an opening line" width="720"></a>

*One translated excerpt from a recorded WorkBuddy sample, highlighting the output fields rather than a decorative cover.*

[Preview sources and capture notes](assets/PREVIEW-SOURCES.md)

- **WorkBuddy Digital Employee Workbench:** turn repeated research, topic selection, formatting, and checking into workflows you can run.
- **Echo:** make room for conversations about life stages, choices, and relationships that you can return to later.
- **AI Cost Copilot:** see where API costs go before choosing models and assembling workflows.

Projects without a public download are labeled in development or in testing. A local build is a different state from a public release.

I also work with the [BFTOOLS team](https://github.com/mercedesbestsupplier-maker) on product direction, user experience, and public product pages, with a current focus on promoting the content-operations tool. [BFTiles](https://github.com/mercedesbestsupplier-maker/BFTiles) was originally developed by [@dingzd1995](https://github.com/dingzd1995).

## What matters to me

- **Start with a real task.** Make one specific thing work well before adding more features.
- **Keep data local when practical.** Projects, agreements, and records that can stay on your computer aren't uploaded by default.
- **Keep key decisions yours.** Replies are reviewed before sending; project scope changes after your confirmation.
- **Be honest about status.** Tests, device verification, signing, notarization, and public release are reported separately.

## Downloads & early access

- [Xiaohongshu NoteSignal: bilingual research extension and early-preview ZIP](https://github.com/LydiaTools/notesignal/releases/tag/v0.1.1)
- [Global Longform SEO Studio: creator-IP article planner and v0.2.0 ZIP](https://github.com/LydiaTools/longform-atlas/releases/tag/v0.2.0)
- [Lydia Foreign Trade System: source and setup](https://github.com/LydiaTools/lydia-foreign-trade-system)
- [CoverCalc Pro: live open-source checker](https://lydiatools.github.io/covercalcpro-landscape-quantity-kit/tools/landscape-volume-check.html) / [full website calculator](https://covercalcpro.com/?utm_source=github&utm_medium=referral&utm_campaign=lydiatools_profile#calculator) / [offline checker v0.1.1 download](https://github.com/LydiaTools/covercalcpro-landscape-quantity-kit/releases/download/v0.1.1/CoverCalcPro-Landscape-Volume-Check-v0.1.1.zip) / [source and formulas](https://github.com/LydiaTools/covercalcpro-landscape-quantity-kit)
- [Say It Plainly: latest download](https://github.com/LydiaTools/shuorenhua/releases/latest)
- [Afdian: tools and updates](https://afdian.com/a/lydiahub2026)
- [Feishu: free product collection](https://jcnrbes3t04e.feishu.cn/drive/folder/VRnafPFVDlcNXrdtpSwcWaWFnEj)
- Bugs and feature ideas: open an Issue in the relevant public repository.
- Early access, custom work, and maintenance: WeChat `lydiahub2026`.

Basic tools will continue to be shared for free. Custom features, deployment help, data migration, and ongoing maintenance can be discussed separately. Some linked interfaces and distribution pages currently use Chinese.

## Find me online

[Facebook · Mercedes Costa](https://www.facebook.com/people/Mercedes-Costa/100074622692401/) · [Quora · MercedesCosta](https://www.quora.com/profile/MercedesCosta) · [TikTok · @covercalcpro](https://www.tiktok.com/@covercalcpro) · [X · MA HIBBERD](https://x.com/LRosamarina)

<a id="最近更新"></a>

## Recent updates

- **2026-10-08:** added Aspectory, a local-first visual post studio with four platform layouts, four styles, and a four-image ZIP export.
- **2026-10-08:** released Xiaohongshu NoteSignal as an early preview and Global Longform SEO Studio as a local bilingual creator-IP writing tool, with source, screenshots, tests and downloadable ZIPs.
- **2026-10-07:** published the CoverCalc Pro landscape kit's first offline HTML download and live open-source checker, with source and a reproducible calculation example; opened the Blueprint synthetic fixture online while keeping the full recovery runner local.
- **2026-10-06:** added Browser Agent Blueprint: original browser-agent prompt modules, a local resume demo, and integration contracts clearly labeled as not live-tested.
- **2026-09-28:** added project links, setup guides, and demos for Lydia Foreign Trade System and the CoverCalc Pro toolkit; linked the English overview for Say It Plainly while keeping existing products, covers, and downloads.
- **2026-09-08:** Scope Check reached its v0.1.0 testing candidate, identifying added work, changed agreements, and questions needing confirmation.
- **2026-09-07:** Say It Plainly v0.9.0 became available through GitHub Releases.
- **2026-09-04:** Desktop Flow updated to Windows v1.0.3, with its core workflow verified on Windows 10 and 11; Mac uses the v1.0.0 DMG.
- **2026-09-04:** reorganized the Afdian page around Desktop Flow, Codex Skin Workshop, and the combined product entry.

---

**A good tool helps you guess less, redo less, and save your energy for the decisions that need you.**
