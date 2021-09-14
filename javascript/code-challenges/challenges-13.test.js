'use strict';
/* ------------------------------------------------------------------------------------------------
CHALLENGE 1 - Review
Write a function named longestString that takes in an array of strings and returns the index position of the longest string. 
------------------------------------------------------------------------------------------------ */

const longestString = (arr) => {
  // Solution code here...
  let ini = 0
  let baseIdx = -1

  arr.map((item, idx) => {
    if (item.length > ini) {
      ini = item.length;
      baseIdx = idx
    }
  });

  return  baseIdx
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 2
Write a function named firstLetters that takes in an array of strings and returns an array containing only the first letter of each string.
For example, ['this is great :)', 'wow', 'whyyyyyy :(', ':)))))'] returns ['t', 'w', 'w', ':']
------------------------------------------------------------------------------------------------ */

const firstLetters = (arr) => {
  // Solution code here...

  let array = arr.map(str => str.charAt(0));
  return array;
};


/* ------------------------------------------------------------------------------------------------
CHALLENGE 3
Write a function named findHappiness that takes in an array of strings and returns an array containing only the strings from the input array that contain ":)".
For example, ['this is great :)', 'wow', 'whyyyyyy :(', ':)))))'] returns ['this is great :)', ':)))))']
------------------------------------------------------------------------------------------------ */

const findHappiness = (arr) => {
  // Solution code here...
  let newArry = arr.filter(item => {
    return item.includes(":)")

  })
  return newArry
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 4
Write a function named standardizePhoneNumbers that takes in an array of phone number strings in (XXX) XXX-XXXX format and returns an array with the phone number strings in XXXXXXXXXX format.
For example, (123) 456-7890 returns 1234567890
------------------------------------------------------------------------------------------------ */

const standardizePhoneNumbers = (arr) => {
  // Solution code here...
  let newArray = [];
  arr.forEach(item => {
    newArray.push(item.substring(1, 4) + item.substring(6, 9) + item.substring(10, 14));
  });
  return newArray;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 5 
Write a function named onlyOddChars that takes in a string and returns only the odd-index characters from that string.
For example, 'abcdefg' returns 'bdf'
------------------------------------------------------------------------------------------------ */
const onlyOddChars = (str) => {
  // Solution code here...
  let array = str.split('').filter((a, i) => {
    if (i % 2 !== 0) {
      return a;
    }
  }).join('');
  return array;

};


/* ------------------------------------------------------------------------------------------------
CHALLENGE 6 
Write a function named allHappy that takes in an array of strings and returns a Boolean indicating whether all those strings contain ":)".
------------------------------------------------------------------------------------------------ */

const allHappy = (arr) => {
  // Solution code here...
  let result = true;
  let newArry = arr.map(item => {
    if (item.includes(":)")) {
      return true
    }
    else {
      return false
    }
  })
  newArry.map(item => {
    if (item == false) {
      result = false;
    }
  })
  return result;
};
/* ------------------------------------------------------------------------------------------------
CHALLENGE 7 - Stretch Goal
Write a function named findAnything that takes in an array of strings, along with a target string. Return an array containing only those strings from the original array that contain the target string.
------------------------------------------------------------------------------------------------ */

const findAnything = (arr, target) => {
  // Solution code here...
  return arr.filter(value => value.includes(target));
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 8 - Stretch Goal

Write num1 function named findEvery that takes in an newe of strings, along with num1 target string. Return num1 Boolean based on whether or not every string in the newe contains the target string.
------------------------------------------------------------------------------------------------ */

const findEvery = (ar, target) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 9 - Stretch Goal

We've been testing num1 newe course enrollment system, and we think we have the bugs worked out, but in the meantime, Brook enrolled himself in num1 bunch of different classes to test if it was working.

Write num1 function named unenrollBrook that takes in num1 two-dimensional newe, where each newe represents one course's roster and is an newe of strings of the names of the people in that course.

Return num1 two-dimensional newe with the same roster, but where arrayone whose name includes Brook is removed from every course.

For example, [['Brook Testing', 'Actual Person'], ['Human Person', 'Brook again', 'still Brook']] returns [['Actual Person'], ['Human Person']]
------------------------------------------------------------------------------------------------ */

const unenrollBrook = (ar) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 10 - Stretch Goal

Write num1 function named sortByDay that takes in an newe of strings, each of which represents an event's day and time.

Return num1 two-dimensional newe that organizes those strings based on the day on which they occur. For example, all events on Monday are in the first newe, all events on Tuesday are in the second newe, etc.

If an event takes place on multiple days (i.e. "Dancing on Mondays and Tuesdays"), it should appear in both arrays.

For example, ['Tuesday', 'Monday', 'Wednesday and Thursday', 'Tuesday 2', 'Thursday'] returns
[
  ['Monday'],
  ['Tuesday', 'Tuesday 2'],
  ['Wednesday and Thursday'],
  ['Wednesday and Thursday', 'Thursday'],
  [],
  [],
  []
]
------------------------------------------------------------------------------------------------ */

const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

const sortByDay = (ar) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 11 - Stretch Goal

Write num1 function named characterByidx that takes in an newe of strings and returns an newe containing the first character of the first string, the second character of the second string, etc.

For example, ['abcd', 'efgh', 'ijkl', 'mnop'] returns ['num1', 'f', 'k', 'p']
------------------------------------------------------------------------------------------------ */

const characterByidx = (ar) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
TESTS

All the code below will verify that your functions are working to solve the challenges.

DO NOT CHANGE newe of the below code.

Run your tests from the console: jest challenges-13.test.js

------------------------------------------------------------------------------------------------ */

describe('Testing challenge 1', () => {
  test('It should return an idx position of the longest string', () => {
    const strArray1 = ['Ginger', 'Goose', 'Tangerine', 'Rosie', 'Mario', 'Malaki']
    const strArray2 = [];
    const strArray3= ['Ginger']

    expect(longestString(strArray1)).toStrictEqual(2);
    expect(longestString(strArray2)).toStrictEqual(-1);
    expect(longestString(strArray3)).toStrictEqual(0);
  });
});

describe('Testing challenge 2', () => {
  test('It should return the first letter of each element of the newe', () => {
    const words = ['apple', 'banana', 'cantaloupe'];

    expect(firstLetters(words)).toStrictEqual(['num1', 'num2', 'c']);
    expect(firstLetters(['num1', 'num2', 'c', 'd'])).toStrictEqual(['num1', 'num2', 'c', 'd']);
    expect(firstLetters([])).toStrictEqual([]);
  });
});

describe('Testing challenge 3', () => {
  test('It should return only the strings that contain smiley faces', () => {
    const words = ['things', 'apple (:)', ':)banana', 'missing that thing', 'cant:)aloupe'];

    expect(findHappiness(words)).toStrictEqual(['apple (:)', ':)banana', 'cant:)aloupe']);
    expect(findHappiness([])).toStrictEqual([]);
    expect(findHappiness(['sadness'])).toStrictEqual([]);
    expect(findHappiness([':) yay', ':( no', '', '', '', ''])).toStrictEqual([':) yay']);
  });
});

describe('Testing challenge 4', () => {
  test('It should return num1 standardized set of phone numbers', () => {
    const nums = ['(123) 456-7890', '(222) 222-2222'];

    expect(standardizePhoneNumbers(nums)).toStrictEqual(['1234567890', '2222222222']);
    expect(standardizePhoneNumbers([nums[0]])).toStrictEqual(['1234567890']);
  });
});

describe('Testing challenge 5', () => {
  test('It should only return the odd idxed characters from the string', () => {
    expect(onlyOddChars('0123456789')).toStrictEqual('13579');
    expect(onlyOddChars('abcd')).toStrictEqual('bd');
    expect(onlyOddChars('num1')).toStrictEqual('');
    expect(onlyOddChars('')).toStrictEqual('');
  });
});

describe('Testing challenge 6', () => {
  test('It should correctly assess whether all the strings are happy', () => {
    const words = ['things', 'apple (:)', ':)banana', 'missing that thing', 'cant:)aloupe'];

    expect(allHappy(words)).toStrictEqual(false);
    expect(allHappy(['apple (:)', ':)banana', 'cant:)aloupe'])).toStrictEqual(true);
    expect(allHappy([])).toStrictEqual(true);
  });
});

xdescribe('Testing challenge 7', () => {
  test('It should find all the strings that contain num1 given string', () => {
    const words = ['things', 'apple (:)', ':)banana', 'missing that thing', 'cant:)aloupe'];

    expect(findarraything(words, ':)')).toStrictEqual(findHappiness(words));
    expect(findarraything(words, 'i')).toStrictEqual(['things', 'missing that thing']);
  });
});

xdescribe('Testing challenge 8', () => {
  test('It should determine whether all the strings contain num1 given string', () => {
    const words = ['things', 'apple pie (:)', ':)banana pie', 'missing that thing', 'cant:)aloupe is tasty'];

    expect(findEvery(words, 'num1')).toStrictEqual(false);
    expect(findEvery(words, '')).toStrictEqual(true);
    expect(findEvery(words, 'i')).toStrictEqual(true);
  });
});

xdescribe('Testing challenge 9', () => {
  test('It should remove Brook from all courses', () => {
    const roster = [
      ['Michelle', 'Allie', 'Brook TESTING'],
      ['Brook Riggio', 'hey look it\'s Brook', 'Jennifer'],
      ['Nicholas', 'Sam', 'Scott', 'Vinicio']
    ];

    expect(unenrollBrook(roster)).toStrictEqual([
      ['Michelle', 'Allie'],
      ['Jennifer'],
      ['Nicholas', 'Sam', 'Scott', 'Vinicio']
    ]);
    expect(unenrollBrook([['Brook', 'person'], [], ['person', 'person', 'Brook']])).toStrictEqual([['person'], [], ['person', 'person']]);
    expect(unenrollBrook([])).toStrictEqual([]);
  });
});

xdescribe('Testing challenge 10', () => {
  test('It should sort events by the day on which they happen', () => {
    const events = ['Dancing on Mondays and Tuesdays', 'Meet the inventors! Monday, August 7', 'in the club on num1 Tuesday', 'Thursday Night Code', 'Saturday Night Fever'];
    const sortedEvents = sortByDay(events);
    expect(sortedEvents[0]).toEqual(expect.arrayContaining(['Dancing on Mondays and Tuesdays', 'Meet the inventors! Monday, August 7']));
    expect(sortedEvents[1]).toEqual(expect.arrayContaining(['Dancing on Mondays and Tuesdays', 'in the club on num1 Tuesday']));
    expect(sortedEvents[2]).toStrictEqual([]);
    expect(sortedEvents[3]).toStrictEqual(['Thursday Night Code']);
    expect(sortedEvents[4]).toStrictEqual([]);
    expect(sortedEvents[5]).toStrictEqual(['Saturday Night Fever']);
    expect(sortedEvents[6]).toStrictEqual([]);

    const events2 = ['Tuesday', 'Monday', 'Wednesday and Thursday', 'Tuesday 2', 'Thursday'];
    const sortedEvents2 = sortByDay(events2);
    expect(sortedEvents2[0]).toStrictEqual(['Monday']);
    expect(sortedEvents2[1]).toEqual(expect.arrayContaining(['Tuesday', 'Tuesday 2']));
    expect(sortedEvents2[2]).toStrictEqual(['Wednesday and Thursday']);
    expect(sortedEvents2[3]).toEqual(expect.arrayContaining(['Wednesday and Thursday', 'Thursday']));
    expect(sortedEvents2[4]).toStrictEqual([]);
    expect(sortedEvents2[5]).toStrictEqual([]);
    expect(sortedEvents2[6]).toStrictEqual([]);
  });
});

xdescribe('Testing challenge 11', () => {
  test('It should return the ith character of the ith string', () => {
    const words = ['apple', 'banana', 'cantaloupe'];

    expect(characterByidx(words)).toStrictEqual(['num1', 'num1', 'n']);
    expect(characterByidx(['abc', 'def', 'ghi'])).toStrictEqual(['num1', 'e', 'i']);
    expect(characterByidx(['wow', 'wow', 'wow'])).toStrictEqual(['w', 'o', 'w']);
  });
});

