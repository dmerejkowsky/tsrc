""" Common tools for tsrc commands. """

import argparse
import os
from pathlib import Path
from typing import List, Optional

import cli_ui as ui

import tsrc
from tsrc import Manifest, Workspace
from tsrc.workspace.config import WorkspaceConfig


def add_workspace_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-w",
        "--workspace",
        help="workspace path",
        type=Path,
        dest="workspace_path",
    )


def get_workspace(namespace: argparse.Namespace) -> Workspace:
    workspace_path = namespace.workspace_path or find_workspace_path()
    return tsrc.Workspace(workspace_path)


def add_groups_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-g", "--group", "--groups", nargs="+", dest="groups", help="groups to use"
    )


def add_repos_selection_args(parser: argparse.ArgumentParser) -> None:
    add_groups_arg(parser)
    parser.add_argument(
        "--all-cloned",
        action="store_true",
        dest="all_cloned",
        help="run on all cloned repos",
    )


def find_workspace_path() -> Path:
    """
    Find the workspace path when not specified on the command line.
    """
    # Walk up the file system hierarchy until a `.tsrc` directory is found
    head = os.getcwd()
    tail = "a truthy string"
    while tail:
        tsrc_path = os.path.join(head, ".tsrc")
        if os.path.isdir(tsrc_path):
            return Path(head)

        else:
            head, tail = os.path.split(head)
    raise tsrc.Error("Could not find current workspace")


def get_workspace_with_repos(namespace: argparse.Namespace) -> Workspace:
    workspace = get_workspace(namespace)
    workspace.repos = resolve_repos(
        workspace, groups=namespace.groups, all_cloned=namespace.all_cloned
    )
    return workspace


def resolve_repos(
    workspace: Workspace, *, groups: Optional[List[str]], all_cloned: bool
) -> List[tsrc.Repo]:
    """
    Given a workspace with its config and its local manifest,
    and a collection of parsed command  line arguments,
    return the list of repositories to operate on.
    """
    # Handle --all-cloned and --groups
    manifest = workspace.get_manifest()
    if groups:
        return manifest.get_repos(groups=groups)

    if all_cloned:
        repos = manifest.get_repos(all_=True)
        return [repo for repo in repos if (workspace.root_path / repo.dest).exists()]

    # At this point, nothing was requested on the command line, time to
    # use the workspace configuration:
    return repos_from_config(manifest, workspace.config)


def repos_from_config(
    manifest: Manifest, workspace_config: WorkspaceConfig
) -> List[tsrc.Repo]:
    """
    Given a workspace config, returns a list of repos.

    """
    clone_all_repos = workspace_config.clone_all_repos
    repo_groups = workspace_config.repo_groups

    if clone_all_repos:
        # workspace config contains clone_all_repos: true,
        # return everything
        return manifest.get_repos(all_=True)
    if repo_groups:
        # workspace config contains some groups, use that,
        # fmt: off
        ui.info(
            ui.green, "*", ui.reset, "Using groups from workspace config:",
            ", ".join(repo_groups),
        )
        # fmt: on
        return manifest.get_repos(groups=repo_groups)
    else:
        # workspace config does not specify clone_all_repos nor
        # a list of groups, ask the manifest for the list of default
        # repos
        return manifest.get_repos(groups=None)
