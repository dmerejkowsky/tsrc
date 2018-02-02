# Development

All the development happens on [GitHub](https://github.com/SuperTanker/tsrc).

Outcome of discussions among maintainers and users of the software are tracked in the [wiki](https://github.com/SuperTanker/tsrc/wiki).


# Reporting bugs and suggesting new features

Feel free to use the [GitHub's bug tracker](https://github.com/SuperTanker/tsrc/issues) to open issues.

If you are reporting a bug, please provide the following information:

* `tsrc` version
* Details about your environment (operating system, Python version)
* The exact command you run
* The full output

Doing so will ensure we can investigate your bug right away.

# Suggesting changes

You are free to open a pull request on GitHub for any feature you'd like.

Before opening a merge request, please read the [code manifesto](https://supertanker.github.io/tsrc/code-manifesto).

Note that for your merge request to be accepted, we'll ask that:

* You follow indications from the code manifesto
* All existing linters pass
* All existing tests run
* The new feature comes with appropriate tests

See the [.travis.yml file](https://github.com/SuperTanker/tsrc/blob/master/.travis.yml)
to see what exactly what commands are run and the Python versions we
support.


# Checking your changes

* Install latest [pipenv](https://docs.pipenv.org/) version.
* Install development and documentation dependencies:

```console
$ pipenv install --dev
```

* Run `setup.py develop` at least once:

```
$ pipenv run python setup.py develop
```

(you should re-run this command every time the `setup.py` file changes).

* Finally, run:

```console
$ pipenv run python ci/ci.py
```


# Adding documentation

* Follow the steps from the [Checking your changes](#checking_your_changes) section to setup your python environment
* Launch the development server locally:

```bash
$ pipenv run mkdocs serve
```

* Edit the markdown files from the `docs/` folder and review the changes in your browser
* Finally, submit your changes by opening a pull request on GitHub