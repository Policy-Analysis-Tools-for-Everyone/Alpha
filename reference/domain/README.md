# Domain-specific reference material

Material about a **particular policy domain**, not about how to do policy
analysis. Nothing here is part of the generic method layer, and no runtime skill
reads it.

The distinction matters because a domain framework sitting next to the generic
methods reads as though it applied to every problem. It doesn't. A capability
skill that absorbed the DPI material would start asking whether a school
admissions problem meets Frischmann's infrastructure criteria.

## `dpi/`: digital public infrastructure and public value

| File | What it is |
|---|---|
| `dpi/dpi-public-value-framework.md` | The project owner's analytical synthesis of the 2 IIPP papers below into a gated framework for judging whether a digital system is infrastructure, and whether it is public |
| `dpi/digital-public-infrastructure-and-public-value.pdf` | Mazzucato, M., Eaves, D. and Vasconcellos, B. (2024), *Digital public infrastructure and public value: What is 'public' about DPI?*, UCL IIPP Working Paper 2024-05 |
| `dpi/economics-of-shared-digital-infrastructures.pdf` | Eaves, D., Coyle, D., Vasconcellos, B. and Deshmukh, S. (2025), *The Economics of Shared Digital Infrastructures: A framework for assessing societal value*, IIPP Policy Report 2025/02 |

**One thing from this material does reach the runtime.** The live disagreement
about whether market failure is the right primary test for public action, or
whether the better question is what direction is embedded in a framing and who
chose it, is carried in the `house-rules` skill as a disagreement the agent
surfaces rather than settles. That is the whole of the domain material's
influence on the generic skills, and it is deliberate: the argument is about
public value in general, not about digital infrastructure in particular.

If a DPI-specific capability is ever wanted, it belongs in a separate skill built
from this material, not folded into the generic ones.
