#!/bin/bash
# Script to compile translation files
# Requires: gettext (msgfmt)

for lang in ru de zh; do
    if [ -f "translations/${lang}/LC_MESSAGES/messages.po" ]; then
        msgfmt -o "translations/${lang}/LC_MESSAGES/messages.mo" "translations/${lang}/LC_MESSAGES/messages.po"
        echo "Compiled ${lang} translations"
    fi
done

echo "All translations compiled!"

