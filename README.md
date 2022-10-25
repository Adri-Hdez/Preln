<p align="center"><img src="https://github.com/Adri-Hdez/Preln/blob/main/static/img/logo.svg" alt="logo" width="80%" /></p>

<p align="center">
 <i>A package for preprocessing text in spanish</i>
</p>


----------------------

<p align="justify">
Preln is a Python package that speeds up development and optimizes the performance of applications that require adequate data processing in the field of NLP (Natural Language Processing). This library takes into account the special characteristics of data written in Spanish. It makes data suitable and ready to use for complex applications like training machine-learning models, extracting content from social media or develop powerful tools to automate language correction, lemmatization, stemming within manny others.
</p>

<p align="center">📃​ <b>Last version v0.5.1-alpha out now!</b> 📃​</p>

# 💬​ Contribution & Questions
| Contribution & Questions Type     | Platforms                               |
| ------------------------------- | --------------------------------------- |
| 🐞​​ **Bug Reports**              | [GitHub Issue Tracker]                  |
| 📦​ **Feature Requests & Ideas** | [GitHub Discussions]                    |
| 🛠️​ **Usage Questions & Discusions**          | [GitHub Discussions] |

# 💼​ Features
- Apply and combine general basic operations to pre-process text in Spanish
- Establish direct connection with file paths, databases… for easy reading and writing data
- Simple implementation, optimized and ready to apply configuration files
- Autocorrect function to improve data quality
- Methods for privacy control, replacing or removing personal data from the dataset
- Support for spanish and english languages

# ​💾​ Install Preln

To start using Preln use the next command:

```markdown
pip install preln
```

Note: you might have to add this command as a “code” line in order to use Preln on a Python notebook.

- [If you are using an old version of Preln, check the update guide to install the package’s new changes.]()

The main object class of the package is called `Preprocessing` and it contains all the principal functions of the package. We will be importing this class and creating and object in order to use it’s methods:

```python
from Preln.preprocessing import Preprocessing

preprocessor = Preprocessing(date=False, date_format=None, accents=False, lowercasing=True,   
               privacy=True, privacy_format="multi:replace", correction=True, media=True, 
               media_format="mention:delete", numbers=False, punctuation=True, 
               stopwords=True, tokenizer=True, debug=False)
```

## 🔧​ Example of use

In this basic example, you can check how to use the package in order to process a simple piece of text.

```python
sample_text = "¡Hola @usuario!, mi nombre es Preln, me han creado Adrián y Raúl. Revisa mi documentación en https://www.preln.org"

test = preprocessor.pipeline(sample_text)

print(test) # ['MENTION', 'nombre', 'ORG', 'creado', 'PERSON', 'PERSON', 'revisa', 'documentación', 'URL']
```

Note: The pipeline method has it´s parameters (which toggle the core methods) setted by default. It’s interesting to change them based on each text we want to process.

- [You can check every option upon the core methods and find out what combination of them suits perfectly with your dataset]()

# 💳​ License
Preln is licensed under [MIT License](LICENSE).

# 🗃️ Shields
<p align="center">
  <a href="https://pypi.org/project/preln/">
    <img src="https://img.shields.io/pypi/v/preln" alt="PyPI" />
  </a>
  <a href="https://pepy.tech/project/preln">
    <img src="https://pepy.tech/badge/preln/month" alt="downloads" />
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="code_format" />
  </a>
</p>
