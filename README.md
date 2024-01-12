# behave-selenium

*This project contains automated tests using the Behave tool and the Selenium automation framework for interactions with the DemoQA website.*

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Features](#features)
- [File Structure](#file-structure)
- [Usage](#usage)

## Introduction

*The project utilizes Behave, a Python behavioral testing library, in conjunction with Selenium, a web testing automation tool.
The goal is to create test scenarios described in natural language (Gherkin) to validate the behavior of a web application (DemoQA).*

---

*O projeto utiliza Behave, uma biblioteca de testes comportamentais em Python, em conjunto com o Selenium, uma ferramenta de automação de testes para aplicações web. 
O objetivo é criar cenários de teste descritos em linguagem natural (Gherkin) para validar o comportamento de um aplicativo web (DemoQA).*


## Setup
*The environment is configured with Selenium's WebDriver to interact with the Chrome browser. The project follows good testing practices, using Gherkin to write scenarios,Behave to execute tests, and Selenium for interactions with the user interface.*

1. Clone the repository:
   ```bash
   git clone https://github.com/amandavical/behave-selenium.git
   cd behave-selenium.git
2. Install the required dependencies:
   ```bash
   pip install selenium
   pip install behave
   pip install gherkin-official

## Features

*The project contains the following test scenarios:*

* Scenario 1 - Verify the main page loading
* Scenario 2 - Verify navigation to the Elements section
* Scenario 3 - Fill and submit the form with valid data
* Scenario 4 - Fill and submit the form with invalid data
* Scenario 5 - Attempt to submit the blank form

---

*O projeto contém os seguintes cenários de teste:*

* Cenário 1 - Verificar o carregamento da página principal
* Cenário 2 - Verificar a navegação para a seção de Elements
* Cenário 3 - Preencher e enviar formulário com dados válidos
* Cenário 4 - Preencher e enviar formulário com dados inválidos
* Cenário 5 - Tentativa de Envio de Formulário em Branco


## File Structure

* features: Contains behavior specification files (.feature files).
* steps: Contains Python files with corresponding test steps ( *_steps.py files).

## Usage
*The project can be executed using Behave, which will interpret the scenarios described in Gherkin and run the tests in the Chrome browser.*


Run the tests using the following command:

```bash
behave
```
The tests will be executed, and the execution report will be displayed in the console.

