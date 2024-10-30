function validParens(s:string[]):boolean {
  const choices = {
    "{": "}",
    "[": "]",
    "(": ")"
  };

  const stack:string[] = [];

  for (let i = 0; i < s.length; i++){
    let val:string = s[i];
    if (choices[stack[stack.length - 1]] === val){
      stack.pop();
    }
    else stack.push(val);
  }

  return stack.length === 0
}