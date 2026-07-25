# Execution modes

One coordinator adapts the repository, ingests the case, facilitates decisions,
freezes contracts, asks for participant count, selects execution mode, and
commits the coordination baseline.

## Main-only

Select when the critical path is small, files/features overlap, contracts may
change, work depends on peer code, or merge overhead will not save time. The
coordinator implements and owns all boundary and end-to-end checks.

## Independent branch fan-out

Select only when at least two outcomes have frozen inputs/outputs,
non-overlapping writable paths, no dependency on unmerged peer code, a
self-contained completion condition, a small local check, and positive
wall-clock savings.

Each packet records user/branch, exact base SHA, one outcome, judge value,
allowed/forbidden paths, frozen contracts, sources/credentials, completion,
small test, commits, handoff, deadline, and kill behavior.

One writable file belongs to one branch. Shared schemas, configuration,
manifests, routing, orchestration, and glue remain with the coordinator.
Workers push commits and handoffs but never merge themselves.

## Sequential integration

The coordinator reviews scope, merges in predefined dependency order, runs a
boundary check after each merge, repairs shared glue narrowly, records results,
and alone proves the integrated end-to-end journey.
