const Generator = require('yeoman-generator');
const glob = require('glob');

module.exports = class extends Generator {
    

    async prompting() {
        this.answers = await this.prompt([
            {
                type: "input",
                name: "name",
                message: "Project name:",
                default: this.appname // Default to current folder name
            },
            {
                type: "confirm",
                name: "cool",
                message: "Are you sure you want to create new project?"
            }
        ]);

        this.log("app name", this.answers.name);
        this.log("cool feature", this.answers.cool);
    }

    writing() {
        // copy all template files and folder structure
        const appName = this.answers.name.toLowerCase().replace(/[\W_]+/g,"_");
        this.fs.copyTpl(
            glob.sync(this.templatePath('**/*'), { dot: true }), 
            this.destinationPath(`${appName}/`), 
            {
                name: appName
            }
        );
    }
};