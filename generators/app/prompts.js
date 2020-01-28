const path = require('path');

module.exports = {
    askForAppName
};

/**
 * @returns default app name
 */
function getDefaultAppName() {
    return /^[a-zA-Z0-9_]+$/.test(path.basename(process.cwd())) ? path.basename(process.cwd()) : 'badong-app';
}

/**
 * Ask a prompt for apps name.
 *
 * @param {object} generator - generator instance to use
 */
async function askForAppName(generator) {
    const defaultAppName = getDefaultAppName();

    generator.answers = await generator.prompt({
        type: 'input',
        name: 'appName',
        validate: input => {
            if (input === 'app') {
                return "Your base name cannot be named 'app' as this is a reserved name for Django";
            }
            return true;
        },
        message: 'What is the base name of your application?',
        default: defaultAppName
    });
}