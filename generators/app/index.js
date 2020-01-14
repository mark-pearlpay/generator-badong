const Generator = require('yeoman-generator');

module.exports = class extends Generator {
    

    async prompting() {
        this.answers = await this.prompt([
            {
            type: "input",
            name: "name",
            message: "Your project name",
            default: this.appname // Default to current folder name
            },
            {
            type: "confirm",
            name: "cool",
            message: "Would you like to enable the Cool feature?"
            }
        ]);

        this.log("app name", this.answers.name);
        this.log("cool feature", this.answers.cool);
    }


    // _prompting() {
    //     return {
    //         askForStuff: function () {
    //             const done = this.async();
            
    //             this.prompt([{
    //                 type: "input",
    //                 name: "name",
    //                 message: "Your project name",
    //                 default: this.appname // Default to current folder name
    //             },
    //             {
    //                 type: "confirm",
    //                 name: "cool",
    //                 message: "Would you like to enable the Cool feature?"
    //             }]).then(prompt => {
    //                 done();
    //             });
    //         },
    //         // askForApplicationType: prompts.askForApplicationType,
    //         // askForModuleName: prompts.askForModuleName
    //     };
    // }

    // get prompting() {
    //     return this._prompting();
    // }

    get method2() {
        return this._method2;
    }

    _method2() {
        this.log('method 2 just ran');
    }

    get method1() {
        return this._method1;
    }

    _method1() {
        this.log('method 1 just ran');
    }

    writing() {
        this.fs.copyTpl(
            this.templatePath('index.html'),
            this.destinationPath(`${this.answers.name}/public/index.html`),
            { title: this.answers.name }
        );
    }
};