![Image of Badong](https://i.pinimg.com/originals/3d/96/31/3d9631a279f53ef1784c8641bb9a2976.jpg)
# Badong - The PearlPay Backend API Code Generator

> Yeoman generator for creating PearlPay backend microservice using python, django and mysql. Lets you quickly set up a project following best practices.

## Usage

Install `yo`, and `generator-badong`:

```ssh
$ npm install -g yo generator-badong
```

### Folder Structure
> We follow onion architecture

    .
    ├── app
    │   ├── application
    │   │   ├── __init__.py
    │   │   ├── services         # Service interface
    │   │   ├── repositories     # Repository interface
    │   │   │   ├── ...
    │   │   └── use_cases        # Interface implementation
    │   │       ├── ...
    │   ├── domain               # Domain entities
    │   │   ├── ...
    │   ├── infrastructure       # Django implementations
    │   │   ├── ...
    │   ├── new_app_name
    │   │   ├── ...
    │   └── requirements.txt
    ├── buildspec.yml
    ├── docker-compose.yml
    ├── Dockerfile
    ├── features                 # BDD feature files
    │   ├── ...
    ├── README.md
    └── tests
        ├── ...


## Generators

Available generators:

* [badong](#app) (aka [badong:app](#app))
* [badong:scaffold](#scaffold)

### App
Sets up a new PearlPay backend microservice, generating all the boilerplate you need to get started.

Usage:
```bash
    $ yo badong
    ? What is the base name of your application? new app name
```

### Scaffold
Generates and wires a model, view, repository and test artifacts.

Example:
```bash
    $ yo badong:scaffold
    ? What is the model name to scaffold? newModel
```

## Team

Badong is beautifully crafted by these people and a bunch of awesome [contributors](https://github.com/PearlEngineering/generator-badong/graphs/contributors)


[![Mark Ranosa](https://secure.gravatar.com/avatar/6b4ddfe5b689d678aa772b592c0b5ab0?s=117)](www.kenranosa.com)|
:---:|
[Mark Ranosa](www.kenranosa.com) | 
