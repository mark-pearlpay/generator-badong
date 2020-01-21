const Generator = require('yeoman-generator');
const glob = require('glob');
const _ = require('lodash');
const fs = require('fs');
const insertLine = require('insert-line');

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

        // Add new model to domains
        // TODO: Refactor me
        let filename = this.destinationPath('app/domain/__init__.py');
        fs.appendFileSync(filename, `from .${nameSnakeCase} import ${namePascalCase}\n`);
        this.log(`${namePascalCase} was appended to ${filename}!`);

        filename = this.destinationPath('app/application/repositories/__init__.py');
        fs.appendFileSync(filename, `from .${nameSnakeCase} import ${namePascalCase}Repository\n`);
        this.log(`${namePascalCase} was appended to ${filename}!`);

        filename = this.destinationPath('app/infrastructure/models/__init__.py');
        fs.appendFileSync(filename, `from .${nameSnakeCase} import ${namePascalCase}Model\n`);
        this.log(`${namePascalCase} was appended to ${filename}!`);

        filename = this.destinationPath('app/infrastructure/modules/__init__.py');
        fs.appendFileSync(filename, `from .${nameSnakeCase} import ${namePascalCase}Module\n`);
        this.log(`${namePascalCase} was appended to ${filename}!`);

        filename = this.destinationPath('app/infrastructure/serializers/__init__.py');
        fs.appendFileSync(filename, `from .${nameSnakeCase} import ${namePascalCase}Serializer\n`);
        this.log(`${namePascalCase} was appended to ${filename}!`);

        filename = this.destinationPath('app/infrastructure/views/__init__.py');
        fs.appendFileSync(filename, `from .${nameSnakeCase} import ${namePascalCase}ViewSet\n`);
        this.log(`${namePascalCase} was appended to ${filename}!`);

        // Register models to django
        filename = this.destinationPath('app/infrastructure/admin.py');
        let data = fs.readFileSync(filename).toString().split('\n');
        let insertIndex = data.indexOf('# Import your models here.') + 2;

        insertLine(filename)
            .contentSync(`from .models import ${namePascalCase}Model`)
            .at(insertIndex);

        data = fs.readFileSync(filename).toString().split('\n');
        insertIndex = data.indexOf('# Register your models here.') + 2;
        insertLine(filename)
            .contentSync(`admin.site.register(${namePascalCase}Model)`)
            .at(insertIndex);
        
        this.log(`Registered ${namePascalCase} Model to Django admin`)

        // Register model to URLs
        filename = this.destinationPath('app/infrastructure/urls.py');
        data = fs.readFileSync(filename).toString().split('\n');
        insertIndex = data.indexOf('from rest_framework.routers import SimpleRouter') + 3;

        insertLine(filename)
            .contentSync(
                `from infrastructure.views import ${namePascalCase}ViewSet\n` +
                `from infrastructure.views.${nameSnakeCase} import ${namePascalCase}ViewsAPI`
                )
            .at(insertIndex);

        data = fs.readFileSync(filename).toString().split('\n');
        insertIndex = data.indexOf('router = OptionalSlashRouter()') + 2;
        insertLine(filename)
            .contentSync(`router.register('${nameDashSeparated}', ${namePascalCase}ViewSet)`)
            .at(insertIndex);

        data = fs.readFileSync(filename).toString().split('\n');
        insertIndex = data.indexOf('urlpatterns = [') + 3;
        insertLine(filename)                
            .contentSync(`\tpath('${nameDashSeparated}/<int:${nameSnakeCase}_id>/increment-view', ${namePascalCase}ViewsAPI.as_view()),`)
            .at(insertIndex);
        
        this.log(`Registered ${namePascalCase} to ${filename}!`)
    }
};