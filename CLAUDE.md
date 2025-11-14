Keep the design document at `./DESIGN.md` up to date when you make changes. The goal of that document is to help AI coding agents work on the codebase. Keep it clean and short, keep the information you think will be most useful to a new AI agent session when starting up.

When you're done with a self-contained change, compile, test, commit, then push.

Do not add workarounds if I didn't ask for them. Do not suppress errors. Do not add conditions that prevent failure when something unexpected happens. Either everything happens as expected, or we get an error and let it percolate up, or we raise an error ourselves.
