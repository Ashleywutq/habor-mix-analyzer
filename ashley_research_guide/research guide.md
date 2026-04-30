the claude session: claude --resume 173c49d9-378b-4808-80d5-cd04b219c2ae
claude command: ANTHROPIC_MODEL=claude-opus-4-7[1m] CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 META_CLAUDE_CODE_RELEASE=latest CLAUDE_CODE_VERSION_OVERRIDE=latest claude --dangerously-skip-permissions --effort max --internet
## overview
we are working on terminal bench adapter project. terminal bench is a terminal benchmark to evaluate agent or llm. in order to create a terminal bench that include many existing benchmarks, we need to translate many existing benchmark into the same format that we can use in terminal using adapter. adapter is a wrapper around existing benchmarks, it will translate existing benchmark into a uniformed format (we call it harbor format). adapter writing part is already done, you can check out https://github.com/harbor-framework/harbor/blob/main/adapters/  to see a list of adapters written. For each adapter, you can checkout adapter_metadata.json for info (example https://github.com/harbor-framework/harbor/blob/main/adapters/adebench/adapter_metadata.json), and checkout parity_experiment.json (example https://github.com/harbor-framework/harbor/blob/main/adapters/adebench/parity_experiment.json) for comparison between original benchmark vs harbor format benchmark.

## My current task
I need to research a list of existing benchmarks, and then output a research result for each benchmark.

## agent benchmarks

| benchmarks   |
| ------------ |
| CRUST-Bench  |
| SWT Bench    |
| cooperbench  |
| devopsgym    |
| AIME         |
| SWE-Lancer   |
| CompileBench |
| GPQA Diamond |
| HumanEvalFix |
| Spider 2     |

## output format 
refer to https://github.com/XiangningLin/habor-mix-analyzer/blob/pipeline/benchmark_info_template.md for the output template 

## how to research 
1. get the benchmark to evaluate
2. find the official website of that benchmark, and read thoroughly 
3. find the original paper for that benchmark, and read thoroughly 
4. find the github for that benchmark, and read the readme
5. find the original leaderboard of that benchmark (not harbor leaderboard), and read thoroughly, make sure to check if there are any sub-leaderboard
6. read the corresponding adapter file under this folder  https://github.com/harbor-framework/harbor/blob/main/adapters/, read parity_experiment.json and adapter_metadata.json throughly to collect info. if adapter is missing or adapter is only translating a sub metric of a benchmark (name can be benchmark_submetric), list in the question section. 
7. after reading all the info, fill the output, create a output file for each benchmark under research folder. naming convention is benmark_name.md for each output answer, quote where you find the answer (e.g. a paragraph in the original paper or website.)
8. if you have any question or uncertain about something, add question section at the bottom of the file.