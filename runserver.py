# Copyright (c) Anish Athalye (me@anishathalye.com)
#
# This software is released under AGPLv3. See the included LICENSE.txt for
# details.

if __name__ == '__main__':
    from uottajudge import app
    import os

    extra_files = []
    if os.environ.get('DEBUG', False):
        app.debug = True
        extra_files.append('./config.yaml')

    app.run(
        host='0.0.0.0',
        port=os.environ.get('PORT', 3030),
        extra_files=extra_files
    )
