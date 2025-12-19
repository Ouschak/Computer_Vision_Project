## Logging

The application writes logs to `app.log`.

### Log rotation (Linux)

For long-running usage, log rotation is recommended.
A sample `logrotate` configuration is provided in:


To enable it on Fedora/Linux:

sudo cp config/logrotate/ai-focus.conf /etc/logrotate.d/ai-focus

