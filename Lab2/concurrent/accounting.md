

# For BASH shells, edit the system-wide BASH runtime config file:

	$ sudo -e /etc/bash.bashrc

# Append to the end of that file:

	export PROMPT_COMMAND='RETRN_VAL=$?;logger -p local6.debug "$(whoami) [$$]: $(history 1 | sed "s/^[ ]*[0-9]\+[ ]*//" ) [$RETRN_VAL]"'

# Set up logging for "local6" with a new file:

	$ sudo -e /etc/rsyslog.d/bash.conf

# And the contents...

	local6.*    /var/log/commands.log

# Restart rsyslog:

	$ sudo service rsyslog restart

# Log out. Log in. Voila!

# But I forgot about log rotation:

	$ sudo -e /etc/logrotate.d/rsyslog

# There is a list of log files to rotate the same way...

	/var/log/mail.warn
	/var/log/mail.err
	[...]
	/var/log/message

# So add the new bash-commands log file in that list:

	/var/log/commands.log

# Save.
