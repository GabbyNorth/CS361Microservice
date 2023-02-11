# Project Title

Microservice: String Generator

## Description

This generator microservice produces a random string of a specified length. The characters include all lowercase and uppercase letters of the alphabet and a random number of spaces in the set.

## Getting Started

### Dependencies

* This microservice relies on string, random and time modules.

### Installing

* The generator microservice can be placed in the main project folder.
* No modifications needed to be made to files/folders.

### Sequence Diagram
![sequenceDiagram](https://user-images.githubusercontent.com/71340905/218283674-4372d6e0-96ad-4796-b9a1-935f451ecb92.jpeg)

* the main program requests the random key string by writing an integer to a textfile.
* The integer is the length of the key requested.
* The generator microservice produces a random string of the specified length.
* The random key is delineated by an asterisk in the beginning and at the end.

```
code blocks for commands
```

## Help

Any errors regarding file path would occur if the generator-service.txt file is placed outside of the main project folder. To avoid this error, please specify the absolute path to the generator-service.txt file or place it in the main project folder.
```
command to run if program contains helper info
```

## Authors

Gabby
[@DGabbyNorth]([https://github.com/GabbyNorth])

## Version History

* 0.1
    * Initial Release

## License

None

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
