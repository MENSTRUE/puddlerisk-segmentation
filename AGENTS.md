# AGENTS.md — PuddleRisk

This document defines the operating rules for coding agents, AI assistants, and contributors working in this repository.

PuddleRisk should grow like a serious ML/CV project:

```text
data
→ evidence
→ model
→ evaluation
→ product
→ documentation
```

not:

```text
idea
→ impressive claim
→ unsupported metric
```

---

## 1. Project Identity

Project:

```text
PuddleRisk
```

Validated task:

```text
Puddle surface instance segmentation from still road images
```

Current champion:

```text
YOLO11s-seg
v2 Stage B
```

Checkpoint:

```text
models/puddlerisk_v2_champion.pt
```

Input size:

```text
640
```

Primary selection metric:

```text
Mask mAP50-95
```

Champion value:

```text
0.4088462879
```

---

## 2. Project Philosophy

Every agent must prioritize:

1. correctness;
2. reproducibility;
3. truthful claims;
4. evidence;
5. maintainability;
6. user usefulness.

Never optimize documentation for hype.

Never optimize metrics by changing the meaning of the task.

---

## 3. Source of Truth

Use repository evidence in this priority order:

```text
reports/final_summary_v2.json
reports/stage_b_metrics.json
reports/dataset_audit_v2.json
reports/v1_v2_comparison.csv
models/puddlerisk_v2_champion.pt
src/
app/
README.md
```

If values disagree:

```text
stop
inspect evidence
resolve discrepancy
update docs
```

Do not choose the larger number.

---

## 4. Current Champion Metrics

Current v2 Stage B metrics:

```text
Box Precision    : 0.7610033019
Box Recall       : 0.7050938338
Box mAP50        : 0.7333168565
Box mAP50-95     : 0.4695096313

Mask Precision   : 0.7645752940
Mask Recall      : 0.6943699732
Mask mAP50       : 0.7248195221
Mask mAP50-95    : 0.4088462879
```

Do not silently round these values in machine-readable files.

Human-facing docs may use percentages with sensible precision.

---

## 5. Claim Boundaries

Allowed claims:

```text
puddle surface segmentation
puddle localization
puddle instance count
predicted mask coverage
detection confidence
```

Disallowed current claims:

```text
puddle depth
water volume
flood severity
hydroplaning probability
accident probability
road risk
physical danger
safety certification
geospatial risk
```

---

## 6. Semantic Rule: Confidence

Confidence means:

```text
model confidence in a predicted instance
```

Confidence does not mean:

```text
severity
danger
risk
depth
probability of accident
```

Never relabel confidence as risk.

---

## 7. Semantic Rule: Coverage

Coverage means:

```text
predicted puddle pixels / total image pixels
```

Coverage is an image-space proxy.

It does not mean:

```text
real puddle area
depth
volume
road severity
flood level
```

---

## 8. Dataset Source

Upstream dataset:

```text
Hanyang University
Puddle Segmentation
Roboflow Universe
```

Official page:

https://universe.roboflow.com/hanyang-university-bd2kb/puddle-segmentation

License:

```text
CC BY 4.0
```

---

## 9. Experiment-Specific Dataset Counts

v2 mounted export:

```text
Train                : 1182
Provided validation  : 293
Clean validation     : 291
Test                 : 0
```

Audit:

```text
Exact cross-split duplicates : 1
Empty train labels            : 19
Empty validation labels       : 5
```

Do not replace these with upstream website counts.

---

## 10. Data Storage Rules

Do not commit raw dataset files by default.

Ignore:

```text
dataset/
dataset_local/
runs/
*.cache
__pycache__/
```

Do not commit temporary training outputs.

Do not commit duplicated datasets.

---

## 11. Annotation Rules

Current task:

```text
single-class instance segmentation
```

Class:

```text
0 = puddle
```

Positive labels must be polygon segmentation labels.

Background images may have empty labels.

Do not convert the project to detection-only unless the task definition is intentionally changed and documented.

---

## 12. Data Audit Requirements

Before any new training run:

```text
[ ] count images
[ ] count labels
[ ] check missing pairs
[ ] check malformed rows
[ ] check duplicate leakage
[ ] check empty labels
[ ] check class IDs
[ ] inspect sample annotations
[ ] define train/val/test protocol
```

No training should start before the data is understood.

---

## 13. Experiment History

v1:

```text
YOLO11n-seg
416 px
Mask mAP50-95 = 0.4039297878
```

v2 Stage A:

```text
YOLO11s-seg
640 px
Mask mAP50-95 = 0.4012571662
```

v2 Stage B:

```text
YOLO11s-seg
640 px
low-LR refinement
Mask mAP50-95 = 0.4088462879
```

v3 exploratory:

```text
YOLO11s-seg
data-centric validation cleaning
Mask mAP50-95 ≈ 0.39975
```

---

## 14. Champion Rule

Current champion:

```text
v2 Stage B
```

A newer experiment does not automatically replace it.

Promotion requires:

```text
direct comparison
same or better evaluation quality
saved metrics
reviewed failure cases
documented decision
```

---

## 15. Primary Metric

Use:

```text
Mask mAP50-95
```

as the primary ranking metric.

Reason:

The product's validated task is segmentation.

---

## 16. Secondary Metrics

Use for diagnostics:

```text
Mask mAP50
Mask Precision
Mask Recall
Box mAP50
Box mAP50-95
Box Precision
Box Recall
Inference latency
```

Do not optimize a secondary metric while ignoring a major primary-metric regression unless the trade-off is explicitly justified.

---

## 17. Validation Terminology

Correct:

```text
clean-validation metrics
```

Incorrect:

```text
test accuracy
test performance
production accuracy
```

The current v2 dataset has no independent test split.

---

## 18. Model Promotion Checklist

Before replacing:

```text
models/puddlerisk_v2_champion.pt
```

require:

```text
[ ] dataset documented
[ ] split documented
[ ] leakage checked
[ ] metrics saved
[ ] primary metric compared
[ ] failure cases inspected
[ ] latency measured if relevant
[ ] README updated
[ ] AGENTS.md updated
[ ] app tested
[ ] model file verified
[ ] commit explains promotion
```

---

## 19. Training Policy

Do not train because:

```text
"we want 90%"
```

Train because:

```text
we have a hypothesis
```

Before training, answer:

```text
What failure are we fixing?
Why should this change help?
What metric decides success?
What data split is used?
What result means failure?
```

---

## 20. Preferred Future Improvement Order

Prefer:

```text
better data
→ better labels
→ independent test
→ robustness analysis
→ calibration
→ architecture changes
```

Avoid:

```text
random hyperparameter sweep
→ bigger model
→ more epochs
→ hope
```

---

## 21. Directory Contract

Repository structure:

```text
app/
assets/
models/
reports/
src/
README.md
AGENTS.md
requirements.txt
LICENSE
.gitignore
```

Each directory has a defined responsibility.

---

## 22. `app/` Contract

`app/` is the UI layer.

Allowed:

```text
file upload
sliders
layout
metrics display
warnings
explanations
```

Not allowed:

```text
duplicated model loading
duplicated mask math
training logic
dataset manipulation
```

---

## 23. `src/model.py` Contract

Responsibilities:

```text
checkpoint path
existence check
YOLO loading
```

Default:

```text
models/puddlerisk_v2_champion.pt
```

Never silently download a fallback model.

---

## 24. `src/inference.py` Contract

Responsibilities:

```text
prediction
mask extraction
box extraction
confidence extraction
instance count
mask union
coverage
structured result
```

Keep independent from Streamlit.

---

## 25. `src/utils.py` Contract

Allowed:

```text
image conversion
formatting
small pure helpers
```

Not allowed:

```text
large business logic
model inference
training
UI state
```

---

## 26. `models/` Contract

Store:

```text
deployment champion checkpoint
```

Do not store:

```text
all epoch checkpoints
every failed experiment
training caches
```

---

## 27. `reports/` Contract

Store machine-readable evidence.

Examples:

```text
JSON metrics
CSV comparisons
audit summaries
prediction summaries
```

Do not manually edit metrics to look better.

---

## 28. `assets/` Contract

Store:

```text
training plots
validation plots
confusion matrices
prediction grids
screenshots
```

Every asset used as evidence must correspond to the experiment being discussed.

---

## 29. Inference Defaults

Current defaults:

```python
imgsz = 640
conf = 0.25
iou = 0.60
retina_masks = True
```

Changing defaults requires documentation.

---

## 30. Inference Output Contract

Expected fields:

```text
annotated_image
instance_count
mask_coverage_pct
confidences
```

Coverage must satisfy:

```text
0 <= mask_coverage_pct <= 100
```

---

## 31. No-Detection Behavior

If no puddle is predicted:

```text
instance_count = 0
mask_coverage_pct = 0
confidences = []
```

The app must not crash.

---

## 32. Multi-Instance Behavior

If multiple puddles are predicted:

- count all predicted instances;
- combine masks using logical union;
- calculate coverage on the union;
- do not double-count overlapping mask pixels.

---

## 33. Color Conversion

Be explicit about:

```text
PIL RGB
OpenCV BGR
Streamlit RGB
```

Avoid accidental red/blue channel inversion.

---

## 34. Dependency Policy

Runtime requirements should remain minimal.

Current expected packages:

```text
ultralytics
streamlit
opencv-python-headless
numpy
Pillow
torch
```

Do not add heavy packages for trivial helpers.

---

## 35. Error Handling

Prefer explicit errors.

Example:

```text
FileNotFoundError:
champion checkpoint not found
```

Avoid silent behavior such as:

```text
missing custom model
→ silently use pretrained COCO model
```

---

## 36. Logging

Runtime logs should be useful but not noisy.

Do not log:

```text
user secrets
API keys
full local paths unnecessarily
private uploaded image data
```

---

## 37. Privacy

Current local app should not add telemetry without explicit documentation.

Future hosted deployments must document:

```text
upload retention
logging
storage
telemetry
third-party services
```

---

## 38. Testing Expectations

Before committing inference changes:

```text
[ ] imports work
[ ] model loads
[ ] normal image works
[ ] no detection works
[ ] multiple detections work
[ ] coverage range valid
[ ] confidence display correct
[ ] Streamlit starts
[ ] image colors correct
```

---

## 39. Recommended Future Tests

Potential test files:

```text
tests/test_model.py
tests/test_inference.py
tests/test_utils.py
tests/test_app_smoke.py
```

---

## 40. Model Loading Test

Test:

```text
models/puddlerisk_v2_champion.pt
```

must exist and load successfully.

Do not mock this path in a way that hides a broken repository checkout.

---

## 41. Coverage Test

Coverage logic must correctly handle:

```text
zero masks
one mask
multiple masks
overlapping masks
```

Union masks must use logical OR semantics.

---

## 42. Confidence Test

Confidence values must remain in:

```text
0 <= confidence <= 1
```

Human display may convert to percentages.

---

## 43. Application Smoke Test

Run:

```powershell
streamlit run app/app.py
```

Confirm:

```text
app starts
model loads
upload works
prediction works
metrics render
```

---

## 44. Documentation Contract

README must document:

```text
task
dataset
license
audit
metrics
scope
limitations
usage
architecture
future work
```

Do not remove limitations to make the project appear stronger.

---

## 45. Dataset Attribution

Keep upstream attribution visible.

Required project-level information:

```text
Hanyang University
Puddle Segmentation
Roboflow Universe
CC BY 4.0
```

Official page:

https://universe.roboflow.com/hanyang-university-bd2kb/puddle-segmentation

---

## 46. License Separation

Code license:

```text
MIT
```

Dataset license:

```text
CC BY 4.0
```

Do not imply the dataset is MIT licensed.

---

## 47. Git Commit Style

Use conventional commits.

Preferred:

```text
feat:
fix:
docs:
refactor:
test:
chore:
```

---

## 48. Good Commit Examples

```text
feat: add puddle segmentation inference pipeline
fix: handle predictions without masks
docs: expand dataset and evaluation documentation
refactor: isolate model loading from Streamlit
test: add mask union edge-case tests
```

---

## 49. Bad Commit Examples

Avoid:

```text
update
fix
day 10
commit
new
final final
```

---

## 50. Main Branch Safety

Do not:

```text
force push main
rewrite history
reset remote main
```

unless explicitly approved.

---

## 51. Generated Artifacts

Do not commit:

```text
runs/
cache/
temporary predictions
large duplicated model checkpoints
```

unless a file has clear repository value.

---

## 52. Secrets

Never commit:

```text
API keys
tokens
passwords
private credentials
.env secrets
```

---

## 53. Experiment Naming

Use names that identify:

```text
model
stage
purpose
```

Example:

```text
stage_b_refine
```

Avoid names like:

```text
final2
final3good
lastfinal
bestbest
```

---

## 54. Report Naming

Prefer:

```text
dataset_audit_v2.json
stage_b_metrics.json
v1_v2_comparison.csv
```

Names should remain understandable months later.

---

## 55. Metric Precision

Machine-readable reports should keep full numeric precision.

README may use:

```text
40.88%
```

for readability.

Do not alter the underlying value.

---

## 56. Screenshot Policy

Screenshots are qualitative evidence.

Never use a single screenshot to claim:

```text
accuracy
mAP
robustness
generalization
```

---

## 57. Failure-Case Policy

Future evaluation should intentionally save:

```text
false positives
false negatives
small puddles
reflections
dark asphalt
shadows
merged masks
fragmented masks
```

Failure cases are part of the portfolio evidence.

---

## 58. Product Copy Rules

Preferred wording:

```text
Detected puddle instances
Predicted mask coverage
Model confidence
```

Avoid:

```text
Danger
Risk level
Flood severity
Safe / Unsafe
```

with the current model.

---

## 59. Road-Risk Feature Rule

A road-risk feature may only be introduced if:

```text
direct risk target exists
labels documented
evaluation defined
failure costs considered
```

Do not derive risk from confidence.

---

## 60. Depth Feature Rule

Do not infer physical depth from 2D segmentation mask area.

A future depth feature requires appropriate sensors or labels.

---

## 61. Video Feature Rule

Video inference is allowed as future functionality.

But frame-level segmentation does not automatically become:

```text
temporal risk prediction
```

Temporal claims require temporal evaluation.

---

## 62. ONNX Export Rule

ONNX export is allowed when useful.

Before documenting ONNX as supported:

```text
export succeeds
runtime loads
predictions compared
latency benchmarked
```

---

## 63. Edge Deployment Rule

Do not call the project edge-ready without:

```text
target hardware
runtime benchmark
memory benchmark
latency benchmark
accuracy comparison
```

---

## 64. API Rule

If an API is added:

```text
core inference stays in src/
API becomes another adapter layer
```

Do not rewrite inference independently inside the API.

---

## 65. Batch Inference Rule

Batch inference should reuse:

```text
same champion
same preprocessing
same output semantics
```

Batch mode must not redefine coverage or confidence.

---

## 66. Training Notebook Rule

Future notebooks should begin with:

```text
heartbeat
environment
dataset audit
```

before expensive training.

---

## 67. Kaggle Rule

For long Kaggle runs:

```text
verify heartbeat
verify dataset path
verify GPU
verify first epoch
then leave unattended
```

Do not wait hours before checking whether the notebook actually started.

---

## 68. Reproducibility Rule

Every promoted model should record:

```text
dataset
split
seed
model
resolution
optimizer
epochs
augmentation
metrics
checkpoint
```

---

## 69. External Benchmark Rule

External benchmark numbers may be discussed.

But do not mix them into project metrics without clearly labeling them as external.

---

## 70. New Dataset Rule

Before combining another dataset:

```text
inspect license
inspect labels
inspect class meaning
inspect annotation format
inspect resolution
inspect domain
```

Do not concatenate datasets only because both contain puddles.

---

## 71. Dataset Merge Rule

A merged dataset requires:

```text
harmonized labels
duplicate check
domain analysis
new split
new benchmark
```

Old metrics are not comparable by default.

---

## 72. Independent Test Rule

Future test data must remain untouched during training decisions.

Do not tune confidence or hyperparameters using test labels.

---

## 73. Calibration Rule

If probabilities are presented as calibrated probabilities, calibration must be explicitly evaluated.

Raw YOLO confidence is not automatically calibrated probability.

---

## 74. Performance Regression Rule

Any change that modifies inference should compare:

```text
correctness
latency
memory
output semantics
```

before being merged.

---

## 75. Refactoring Rule

Refactors should not silently change prediction behavior.

If behavior changes, classify the commit accordingly and test it.

---

## 76. UI Rule

UI improvements must not change metric meaning.

A prettier gauge does not justify changing:

```text
coverage
```

into:

```text
risk
```

---

## 77. Accessibility Rule

Future UI improvements should consider:

```text
clear labels
readable contrast
text explanations
not relying only on color
```

---

## 78. Error Message Rule

Errors should tell the developer what to fix.

Bad:

```text
Something went wrong
```

Better:

```text
Model checkpoint not found at models/puddlerisk_v2_champion.pt
```

---

## 79. Performance Target Rule

Do not set arbitrary goals such as:

```text
must reach 90%
```

without understanding the metric.

For segmentation:

```text
mAP50-95
```

is not directly comparable to classification accuracy.

---

## 80. Scientific Honesty Rule

Failed experiments stay valid evidence.

Do not delete v3 history simply because it did not win.

The project should show:

```text
hypothesis
experiment
result
decision
```

---

## 81. Before → Now → Next Rule

Documentation should keep clear separation between:

```text
Before
Now
Next
```

Do not describe planned work as completed functionality.

---

## 82. Future Work Language

Use:

```text
planned
possible
candidate
future direction
```

for unimplemented features.

Do not use:

```text
supports
provides
includes
```

unless the code exists.

---

## 83. Definition of Done

A change is done when:

```text
1. code runs
2. scope remains correct
3. tests/checks pass
4. docs match behavior
5. metrics remain honest
6. repository stays clean
7. commit explains the change
```

---

## 84. Pull Request Review Questions

Ask:

```text
Does this change alter model behavior?
Does it alter output meaning?
Does it alter dataset assumptions?
Does it alter metrics?
Does it add dependencies?
Does it affect licensing?
Does README need update?
Does AGENTS need update?
```

---

## 85. Champion Replacement Decision

Champion replacement is a project-level decision.

Do not casually overwrite:

```text
models/puddlerisk_v2_champion.pt
```

---

## 86. Long-Term Direction

The long-term project direction is:

> reliable visual road-surface observation

Possible components:

```text
segmentation
video analytics
deployment
monitoring
```

Physical risk should remain separate until supported by data.

---

## 87. Final Agent Principle

Always distinguish:

```text
what the image shows
what the model predicts
what the benchmark measures
what the product claims
```

If these four things drift apart, stop and fix the project definition before adding more features.

---

## 88. Final Rule

> **Do not make the project sound smarter than the evidence. Make the evidence stronger.**
