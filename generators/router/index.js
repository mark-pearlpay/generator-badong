const Generator = require('yeoman-generator');

module.exports = class extends Generator {
    get method1() {
        return this._method1;
    }

    _method1() {
        this.log('method 1 just ran');
    }

    get method2() {
        return this._method2;
    }

    _method2() {
        this.log('method 2 just ran');
    }

    async prompting() {
        this.answers = await this.prompt([
            {
            type: "input",
            name: "name",
            message: "name?",
            default: this.appname // Default to current folder name
            },
            {
            type: "confirm",
            name: "cool",
            message: "Add new file?"
            }
        ]);

        this.log("app name", this.answers.name);
        this.log("cool feature", this.answers.cool);
    }

    writing() {
        this.fs.copyTpl(
            this.templatePath('index.py'),
            this.destinationPath('src/index.py'),
            { foo: this.answers.name }
        );
    }
};