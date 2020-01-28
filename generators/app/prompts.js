/**
 * Copyright 2020-2020 the original author or authors from the Badong project.
 *
 * This file is part of the Badong project.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
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
        default: getDefaultAppName()
    });
}