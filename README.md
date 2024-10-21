# python-aaa-sample
Sample repository to start a project with strong gatekeeping tools

## History

This repository was originally created as a support for a training I was providing in 2019.

The main aspect of the training was about development best practices and was about the same motto I've kept over years when starting a project:

> When you start a project with the proper quality target,
> it's easier to keep it, than having to reach it later on.

Technology has evolved faster than this repository, but I've kept it as reference.

Here we are a few years later and a bit of refresh of technologies. Best-practices haven't changed though.

## Toolbox

### TDD

Using [pytest](https://docs.pytest.org/en/stable/contents.html) and `pytest-cov` to get your tests running and a proper coverage measure.

> Coverage is a measure, not a KPI,
> however if you write tests in advance to get clarify expectations
> and if you start with a measurement, it can stay meaningful

Start at 100%, developers will enjoy keeping at 100%, start lower, the developers will find ways to work around the bar and the code will suffer

### Formatting

> When working alone, a formatting tool may seem useless. When you start collaborating, formatting is key to reducing SCM conflicts.
>
> Don't forget you're always collaborating with your future self.

After years of using [`Black`](https://black.readthedocs.io/en/stable/), I now recommend using [`Ruff`](https://docs.astral.sh/ruff/formatter/). Both work find, but `ruff` does both format and linting, hence a slightly smaller dependency bundle.
For the same reason I've now discarded `isort` for `ruff`

### Linting

If you landed on this repository, you must have heard about cognitive complexity, or you have suffered of poor syntax usage that developers do not realize induce poorer performances.

For this stage, I'm usually in favour of combining all the tools that may be complementary, [`Pyflakes`](https://github.com/PyCQA/pyflakes), [`Pylint`](https://github.com/pylint-dev/pylint).
Yet after years of hegemony of these tools, `ruff` has done a great job catching up. Cherry on the cake, `ruff` offers to automatically fix some common mistakes for you.

> Tip: Linters have rules defined and maintained by a worldwide community.
> Keep the rules and deviate from them as little as you can.

### Typing

I've worked with Python 2 for over 10 years, and for as long I've suffered from so many errors of inputs not passed as expected.

Do yourself a favor: invest well your time defining your inputs.
Your brains will thank you for the hours saved investigating problems of inputs.

[`mypy`](https://mypy.readthedocs.io/en/stable/) is the undisputed static type analyzer.


## Shift left

CI is the right place to make the validation of the code when it's ready to be reviewed. The first line of defense against "It worked on my machine" arguments.
However, CI is costly and I've seen a lot of waste from developers waiting for CI to yield tests results and iterate back and forth.

That's why I advise for a full shift-left mindset, using [`pre-commit`](https://pre-commit.com/).

It's a debate in the industry whether or not a commit operation should be instantaneous or not. I'm on the side of saying that unit tests should be fast and that it's better to take a minute or two in the commit phase rather than waiting 10 minutes to see it fail in CI.
However, this is obviously a game of balance, and you have to find your own.

## Dependency management

I'm currently using this repository to test [`uv`](https://docs.astral.sh/uv/) but for me it's still too fresh for production use.

