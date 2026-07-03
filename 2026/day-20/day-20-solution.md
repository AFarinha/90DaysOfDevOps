# Day 20 Solution

## Approach

`log_analyzer.sh` validates the input log file, counts error lines, extracts critical events and writes a dated report.

## Commands and Tools Used

- `grep`: filter errors and critical lines.
- `wc`: count total lines.
- `sort` and `uniq -c`: calculate top repeated errors.
- `sed`: clean output formatting.
- `date`: generate the report filename.

## Sample Run

```bash
./sample_logs_generator.sh sample_log.log 200
./log_analyzer.sh sample_log.log
cat log_report_$(date +%Y-%m-%d).txt
```

## What I Learned

- Log analysis can be automated with basic Unix tools.
- Input validation makes scripts safer.
- Reports should include both totals and specific evidence.

