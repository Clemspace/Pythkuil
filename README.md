# Pythkuil

This project is a Python-based toolkit for working with the New Ithkuil language, a highly sophisticated constructed language designed for precise and unambiguous communication. This toolkit is specifically related to Ithkuil III and IV, the latest versions of the language.

## Project Structure

```
Pythkuil/
│
├── grammar/
│   ├── init.py
│   ├── cases.py
│   ├── formative.py
│   ├── word_types/
│   │   ├── init.py
│   │   ├── adjunct.py
│   │   ├── formative.py
│   │   ├── ithkuil_word.py
│   │   ├── numerical.py
│   │   ├── referential.py
│   │   └── special_construct.py
│   └── parsers/
│       ├── init.py
│       ├── formative_parser.py
│       └── ithkuil_parser.py
│
├── morphology/
│   ├── init.py
│   ├── affiliation.py
│   ├── affix.py
│   ├── ca_complex.py
│   ├── configuration.py
│   ├── context.py
│   ├── essence.py
│   ├── extension.py
│   ├── function.py
│   ├── perspective.py
│   ├── phonology.py
│   ├── slots.py
│   ├── specification.py
│   ├── stem.py
│   └── version.py
│
├── lexicon/
│   ├── init.py
|   ├── affix.py
│   ├── root.py
│   ├── root_database
│   └── test_lexicon.py
│
├── resources/
│   ├── newithkuil_affixes.pdf
│   ├── newithkuil_lexicon.pdf
│   ├── New Ithkuil Single Page Cheat Sheet.pdf
│   ├── The New Ithkuil Cheatsheet (with definitions).pdf
|   └── Lexicon.json
│
├── utils/
│   ├── init.py
│   ├── shortcuts.py
│   └── pdf_parser.py
│
├── init.py
├── .gitignore
├── LICENSE
└── README.md
```

## Roadmap

### Milestone 1: Core Language Structures
- [ ] Implement base classes for fundamental Ithkuil concepts
- [ ] Create enums for all categorical values
- [ ] Develop utility functions for phonological rules

### Milestone 2: Lexicon and Affix Database
- [ ] Parse lexicon PDF to extract roots and meanings
- [ ] Create database structure for roots and stems
- [ ] Parse affix PDF and implement lookup system

### Milestone 3: Word Formation
- [ ] Implement methods to generate valid Formatives
- [ ] Create functions for applying affixes
- [ ] Develop methods for concatenation and incorporation
- [ ] Implement stress assignment rules

### Milestone 4: Parsing and Validation
- [ ] Create parser for Ithkuil words
- [ ] Implement validation rules
- [ ] Develop error reporting system
- [ ] Create detailed word breakdown system

### Milestone 5: Sentence-Level Structures
- [ ] Implement classes for case-frames and case-accessors
- [ ] Develop methods for sentence structure and word order
- [ ] Create system for register and bias adjuncts
- [ ] Implement sentence-level parsing and validation

### Milestone 6: Semantic Interpretation
- [ ] Develop system for semantic interpretation
- [ ] Create methods to combine meanings of roots, stems, and affixes
- [ ] Implement system for handling nuanced meanings

### Milestone 7: Corpus Generation Tools
- [ ] Develop methods to generate valid Ithkuil words and sentences
- [ ] Create system for translating simple concepts into Ithkuil
- [ ] Implement tools for expanding simple sentences into complex ones

### Milestone 8: Language Model Integration
- [ ] Create data generation pipeline for training language models
- [ ] Implement methods to validate and correct generated Ithkuil text
- [ ] Develop tools to analyze semantic accuracy of generated text
- [ ] Create system for fine-tuning language models on Ithkuil data

### Milestone 9: User Interface and Documentation
- [ ] Develop command-line interface
- [ ] Create comprehensive documentation
- [ ] Implement simple web interface
- [ ] Create tutorials and examples

### Milestone 10: Testing and Refinement
- [ ] Develop comprehensive test suite
- [ ] Implement performance optimizations
- [ ] Refine error handling and user feedback
- [ ] Conduct thorough testing with complex Ithkuil constructions

## Contributing

Contributions to this project are welcome. Please feel free to submit pull requests or open issues to discuss potential improvements or report bugs.

To contribute:
1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is based on the work of John Quijada, the creator of the Ithkuil language. We acknowledge his incredible contribution to the field of constructed languages.

## References

- [Official Ithkuil Website](http://www.ithkuil.net/)
- [Ithkuil Subreddit](https://www.reddit.com/r/Ithkuil/)
- [Ithkuil Discord Server](https://discord.gg/WgFrX8J)
- [Complete Ithkuil Lexicon](https://github.com/yuorb/lexicon-json)
