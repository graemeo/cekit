import os

from cekit import tools
from cekit.descriptor import Module
from cekit.module import modules

module_desc = {
    'schema_version': 1,
    'name': 'master_mod',
    'modules': {
        'repositories': [{
            'name': 'module',
            'path': 'tests/modules/repo_1',
        },
        ]
    }
}


def setup_function(function):
    tools.cfg = {}
    tools.cfg['common'] = {'work_dir': '/tmp'}


def test_modules_repos(tmpdir):
    tmpdir = str(tmpdir.mkdir('target'))
    module = Module(module_desc, os.getcwd(), '/tmp')
    module.fetch_dependencies(tmpdir)
    assert 'foo' in [m['name'] for m in modules]
