from .core.punctuation import punctuation_es
from .core.numbers import numbers_cleanner
from .core.autocorrect import autocorrect
from .core.lowercasing import lowercasing
from .core.stopwords import stopwords_es
from .core.tokenizer import tokenizer
from sqlalchemy import create_engine
from .core.accents import accents
from .core.privacy import privacy
from distutils.log import error
from .core.media import media
from .core.date import date

import pandas as pd
import sqlalchemy
import logging
import os


class Preprocessing:
    """Preln main class. Preprocess a given spanish text.
    Use pipeline(), pipelineFile() or databasePipeline() to use the package.
    """

    def __init__(
        self,
        date=False,
        date_format=None,
        accents=False,
        lowercasing=True,
        privacy=False,
        privacy_format="multi:delete",
        correction=False,
        media=False,
        media_format="multi:delete",
        numbers=True,
        punctuation=True,
        stopwords=True,
        tokenizer=True,
        debug=False,
    ):
        """Preprocessing class constructor.
        Initialize and custom pre-processing pipeline.

        Args:
          date (bool, optional): Date formatter or delete date from text. Defaults to False.
          date_format (string, optional): Type of date format [complete, month, month_year, eliminate]. Defaults to None.
          accents (bool, optional): Accents cleanner from [Árbol] to [Arbol]. Defaults to False.
          lowercasing (bool, optional): Lowercase text. Defaults to True.
          numbers (bool, optional): Delete numbers pattern. Defaults to True.
          punctuation (bool, optional): Delete text punctuation [Spanish punctuation included]. Defaults to True.
          stopwords (bool, optional): Delete and clean dont wanted words in text. Defaults to True.
          tokenizer (bool, optional): Transform string to list (to summ up). Defaults to True.
          debug (bool, optional): Displays the code execution log by console. Defaults to False.
        """
        self.__date = date
        self.__date_format = date_format
        self.__accents = accents
        self.__lowercasing = lowercasing
        self.__privacy = privacy
        self.__privacy_format = privacy_format
        self.__correction = correction
        self.__media = media
        self.__media_format = media_format
        self.__numbers = numbers
        self.__debug = debug
        self.__punctuation = punctuation
        self.__stopwords = stopwords
        self.__tokenizer = tokenizer

    def pipeline(self, text) -> str:
        """Pre-processes a given text by
        applying the different pre-processing methods.

        Args:
          text (str): Text to be pre-processed.

        Returns:
          str: Pre-processed text.
        """
        if self.__debug:
            logging.basicConfig(
                level=logging.DEBUG, format="%(asctime)s | %(levelname)8s | %(message)s"
            )
        logging.debug("> Starting preprocessing pipeline...")

        # Preprocessing pipeline creation
        try:
            if self.__date:
                text = date(text=text, type=self.__date_format, debug=self.__debug)
            if self.__accents:
                text = accents(text=text, debug=self.__debug)
            if self.__lowercasing:
                text = lowercasing(text=text, debug=self.__debug)
            if self.__privacy:
                text = privacy(
                    text=text, format=self.__privacy_format, debug=self.__debug
                )
            if self.__correction:
                text = autocorrect(text=text, debug=self.__debug)
            if self.__media:
                text = media(text=text, format=self.__media_format, debug=self.__debug)
            if self.__numbers:
                text = numbers_cleanner(text=text, debug=self.__debug)
            if self.__punctuation:
                text = punctuation_es(text=text, debug=self.__debug)
            if self.__stopwords:
                text = stopwords_es(text=text, debug=self.__debug)
            if self.__tokenizer:
                text = tokenizer(text=text, debug=self.__debug)

            logging.debug("Preprocessing pipeline completed! <")
            logging.debug("")

            return text

        except TypeError:
            error("ERROR: Given text type must be a unique string!")
            logging.debug("Preprocessing pipeline failed! <")
            logging.debug("")

    def filePipeline(self, filePath, key) -> list:
        """Pre-processes a given file by
        applying the different preprocessing methods.

        Args:
          filePath (str): The file to be pre-processed.
          key (str): Dataframe key(column).

        Returns:
          list: A list of the contents of the pre-processed file.
        """
        if self.__debug:
            logging.basicConfig(
                level=logging.DEBUG, format="%(asctime)s | %(levelname)8s | %(message)s"
            )
        logging.debug("> Starting preprocessing pipeline...")

        try:
            split_path = os.path.splitext(filePath)
            ext = split_path[1].replace(".", "")

            if ext == "csv":
                df = pd.read_csv(filePath)
            if ext == "xml":
                df = pd.read_xml(filePath)
            if ext == "excel":
                df = pd.read_excel(filePath)
            if ext == "json":
                df = pd.read_json(filePath)

            texts = df[key].values.tolist()
            array = []

            for text in texts:
                text = self.pipeline(text)
                array.append(text)

            logging.debug("Preprocessing pipeline completed! <")
            logging.debug("")

            return array

        except UnboundLocalError:
            error(
                "ERROR: Take care with file path extension, must be one of these: .csv .xml .json .xlsx!"
            )
            logging.debug("Preprocessing pipeline failed! <")
            logging.debug("")
        except FileNotFoundError:
            error("ERROR: File path does not exists, check function arguments!")
            logging.debug("Pre-processed data file creation failed! <")
            logging.debug("")
        except TypeError:
            error("ERROR: Given file path type must be a unique string!")
            logging.debug("Preprocessing pipeline failed! <")
            logging.debug("")
        except KeyError:
            error(
                "ERROR: Given dataframe key(column) must be a unique string and must exist in the dataframe!"
            )
            logging.debug("Preprocessing pipeline failed! <")
            logging.debug("")

    def databasePipeline(
        self, hostname, username, password, dbname, port, table, key
    ) -> list:
        """Pre-processes a SQL database by
        applying the different preprocessing methods.

        Args:
          hostname (str): DB host name.
          username (str): DB user name.
          password (str): DB user password.
          dbname (str): DB name.
          port (str): DB port.
          table (str): Table created in the DB.
          key (str): Table key(column).

        Returns:
          list: A list of the contents of the pre-processed file.
        """
        if self.__debug:
            logging.basicConfig(
                level=logging.DEBUG, format="%(asctime)s | %(levelname)8s | %(message)s"
            )
        logging.debug("> Starting preprocessing pipeline...")

        try:
            connect_info = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{dbname}?charset=utf8"
            engine = create_engine(connect_info, pool_pre_ping=True)

            # SQL Command and execution
            sql_cmd = f"SELECT * FROM {table}"
            df = pd.read_sql(sql=sql_cmd, con=engine)

            texts = df[key].values.tolist()
            array = []

            for text in texts:
                text = self.pipeline(text)
                array.append(text)

            logging.debug("Preprocessing pipeline completed! <")
            logging.debug("")

            return array

        except sqlalchemy.exc.OperationalError:
            error("ERROR: Take care with your database info, check function arguments!")
            logging.debug("Preprocessing pipeline failed! <")
            logging.debug("")
        except sqlalchemy.exc.ProgrammingError:
            error("ERROR: There is a problem with your table name, it does nbt exists!")
            logging.debug("Pre-processed data file creation failed! <")
            logging.debug("")
        except KeyError:
            error(
                "ERROR: Given dataframe key(column) must be a unique string and must exist in the dataframe!"
            )
            logging.debug("Preprocessing pipeline failed! <")
            logging.debug("")

    def write(
        self, textList, originalFilePath=None, outputFilePath="./preprossedText.csv"
    ) -> None:
        """Convert pre-processed text list to a csv file
        or override original file adding pre-processed text.

        Args:
          textList (list): list with pre-processed text.
          originalFilePath (str, optional): Original file, containing text without pre-processed text. Defaults to None.
          outputFilePath (str, optional): Output file. Defaults to './preprossedText.csv'.

        Raises:
          Exception: handle if textList is not a list.
        """
        if self.__debug:
            logging.basicConfig(
                level=logging.DEBUG, format="%(asctime)s | %(levelname)8s | %(message)s"
            )
        logging.debug("> Creating new file...")

        try:
            if type(textList) != list:
                raise Exception
            try:
                if originalFilePath == None:
                    df = pd.DataFrame()
                    df["text"] = textList
                    df.to_csv(outputFilePath, index=False)
                else:
                    split_path = os.path.splitext(originalFilePath)
                    ext = split_path[1].replace(".", "")

                    if ext == "csv":
                        df = pd.read_csv(originalFilePath)
                    if ext == "xml":
                        df = pd.read_xml(originalFilePath)
                    if ext == "excel":
                        df = pd.read_excel(originalFilePath)
                    if ext == "json":
                        df = pd.read_json(originalFilePath)

                    df["preprocessed_text"] = textList
                    df.to_csv(outputFilePath, index=False)

            except UnboundLocalError:
                error(
                    "ERROR: Take care with file path extension, must be one of these: .csv .xml .json .xlsx!"
                )
                logging.debug("Pre-processed data file creation failed! <")
                logging.debug("")
            except FileNotFoundError:
                error(
                    "ERROR: Input/Ouput file path does not exists, check function arguments!"
                )
                logging.debug("Pre-processed data file creation failed! <")
                logging.debug("")
            except TypeError:
                error("ERROR: Given input/output file path type must be a string!")
                logging.debug("Pre-processed data file creation failed! <")
                logging.debug("")
            else:
                logging.debug("Pre-processed data file created! <")
                logging.debug("")
        except:
            error("ERROR: Given pre-processed data must be a list!")
            logging.debug("Pre-processed data file creation failed! <")
            logging.debug("")
