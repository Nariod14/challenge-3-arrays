# Challenge 03: Array Duplicator

## Overview
Working with arrays is a fundamental skill in JavaScript. In this challenge, you'll create utility functions to handle array duplicates in different ways.

For this challenge, you need to write three functions that:
1. Find all duplicate values in an array
2. Remove all duplicates from an array
3. Count how many times each value appears

### Examples:
```javascript
// 1. Find duplicates
findDuplicates([1, 2, 3, 2, 4, 1])  
// returns [1, 2]

// 2. Remove duplicates
removeDuplicates([1, 2, 3, 2, 4, 1])  
// returns [1, 2, 3, 4]

// 3. Count occurrences
countOccurrences([1, 2, 3, 2, 4, 1])  
// returns { '1': 2, '2': 2, '3': 1, '4': 1 }
```

## Rules
Follow the same Git workflow practices we established:

1. Fork this repo to your own Git
2. Create your working branch using this naming convention:
   - `feat/` - for the main work
   - `fix/` - for things you need to improve
   - `chore/` - for things you need to clean up

Example:
```bash
git checkout -b feat/CC-challenge-3-array-duplicator
```

## Requirements
- Functions should handle different types of arrays:
  - Numbers
  - Strings
  - Mixed types
- Write tests for your solution
- Think about edge cases:
  - Empty arrays
  - Arrays with one element
  - Arrays with all duplicate elements
  - Arrays with no duplicates
  - Handling null/undefined values

## Project Setup
```bash
npm init -y
npm install --save-dev jest
npm install --save-dev eslint prettier
```

Update your package.json with:
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "lint": "eslint .",
    "format": "prettier --write ."
  }
}
```

## Tips
- Consider using different JavaScript methods like:
  - Set
  - Map
  - filter()
  - reduce()
- Think about performance for larger arrays

## Submission
- Complete your solution
- Merge everything into main
- Post your solution link in the challenge thread

Good luck! 🎯 