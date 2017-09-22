# Changelog

## v0.3.0


* *Breaking change*: Add support for groups (#30). Reported by @arnaudgelas

### Upgrading from v0.2.4

To upgrade from an older version of `tsrc`, you should re-run `tsrc init` with the correct url:

```console
# Check manifest URL:
$ cd <workspace>/.tsrc/manifest
$ git remote get-url origin
# Note the url, for instance ssh://git@example.com:manifest.git
$ cd <workspace>
$ tsrc init <manifest-url>
```

This is required to create the `<workspace>/.tsrc/manifest.yml` file which is later used by `tsrc sync` and other commands.


## v0.2.4 (2017-07-13)

* `tsrc push --assignee`: fix when there are more than 50 GitLab users (#25). Reported by @arnaudgelas

## v0.2.3 (2017-09-01)

* Split user interface functionality into its own project: [python-cli-ui](https://github.com/TankerApp/python-cli-ui).

* Add `--quiet` and `--color` global options.

## v0.2.2 (2017-08-22)

Bug fix release.

* `tsrc init`: Fix crash when a repository is empty (#17). Reported by @nicolasbrechet
* `tsrc push`: Fix rude message when credentials are missing (#20). Reported by @cgestes

## v0.2.1 (2017-08-10)

Packaging fixes.


## v0.2.0 (2017-08-09)

* Support for specifying custom branches in the manifest
* Support for specifying fixed refs (tags or hashes) in the manifest

New syntax is:

```yaml
repos:
  - src: foo
    url: git@gitlab.com:proj/foo
    branch: next

  - src: bar
    url: git@gitlab.com:proj/bar
    branch: master
    ref: v0.1
```

Note that `branch` is still required.

* You can now skip the `dest` part of the `copy` section if `src` and `dest` are
  equal:

```yaml
copy:
  - src:foo

# same thing as
copy:
 - src: foo
   dest: foo
```


## v0.1.4 (2017-08-04)

Support for Python 3.3, 3.4, 3.5 and 3.6

## v0.1.1 (2017-08-02)

First public release
