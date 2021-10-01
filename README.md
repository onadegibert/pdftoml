# pdf2ml

## Project description

pdftoml is a script that allows you to convert pdf files to plain text ready to use for machine learning.

## Install and run

### Virtual environment

pdf2ml was built and tested with Python3.7. It should work for Python >= 3.6 but it has not been tested with other versions than 3.7.

For creating the virtual environment and installing the dependencies (from `requirements.txt`), run:

```sh
bash setup.sh
```

With the virtual environment activated (`source venv/bin/activate`), run the following with the python interpreter:

```sh
(venv) $ python src/pdf2ml.py input_dir output_dir language
```
### Examples

In the `test/` directory, there is a pdf of the Spanish Constitution in Catalan.

We could run the following command:

```sh
(venv) $ python src/pdftoml.py test out ca
```

The output will be stored in `out/` directory.

## Contributing

Pull requests are welcome!

## Authors

* [Casimiro Pio Carrino](https://github.com/ccasimiro88)
* [Ona de Gibert](https://github.com/onadegibert)

## License

This project is licensed under the [MIT License](LICENSE).
