function isPalindrome(s: string): boolean {
  const c = s.toLowerCase().replace(/\W+|_/g, '')
  let l = 0;
  let r = c.length - 1;
  while (l < r){
    let lc = c[l];
    let rc = c[r];

    if (lc != rc) return false;
    l++;
    r--;
  }

  return true;
};