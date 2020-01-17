const Generator = require('yeoman-generator');
const glob = require('glob');
const _ = require('lodash');
const fs = require('fs');

module.exports = class extends Generator {
    

    async prompting() {
        this.answers = await this.prompt([
            {
                type: "input",
                name: "name",
                message: "Model name:",
                default: this.appname // Default to current folder name
            },
            {
                type: "confirm",
                name: "cool",
                message: "Are you sure you want to scaffold new model?"
            }
        ]);

        this.log("app name", this.answers.name);
        this.log("cool feature", this.answers.cool);
    }

    writing() {
        // copy all template files and folder structure
        const nameSnakeCase = this.answers.name.toLowerCase().replace(/[\W_]+/g,"_");
        const nameDashSeparated = this.answers.name.toLowerCase().replace(/[\W_]+/g,"-");
        const nameCamelCase = _.camelCase(this.answers.name);
        const namePascalCase = _.upperFirst(_.camelCase(this.answers.name));
        this.fs.copyTpl(
            glob.sync(this.templatePath('**/*'), { dot: true }), 
            this.destinationPath('app/'), 
            {
                name: this.answers.name,
                nameDashSeparated: nameDashSeparated,
                nameSnakeCase: nameSnakeCase,
                nameCamelCase: nameCamelCase,
                namePascalCase: namePascalCase
            }
        );

        // TODO write in files the needed imports T_T
        fs.appendFile(this.destinationPath('app/domain/__init__.py'),
            `from .${nameSnakeCase} import ${namePascalCase}`, (err) => {
            if (err) throw err;
            // this.log('The "data to append" was appended to file!');
        });
    }
};