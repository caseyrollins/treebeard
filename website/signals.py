"""Consolidates all signals used by the OSF."""

from framework.auth import signals as auth
from website.project import signals as project
from website.addons.base import signals as event

ALL_SIGNALS = [
    auth.contributor_removed,
    auth.node_deleted,
    project.unreg_contributor_added,
    project.contributor_added,
    auth.user_confirmed,
    auth.user_email_removed,
    auth.user_registered,
    auth.user_merged,
    event.file_updated,
]
