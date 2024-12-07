'''

 1 - 2 - 3 - 4

 dummy = {
  next:
}

node = head
prev = dummy

while node and node.next:
  1 -> 3 => first.next = second.next
  2 -> 1 -> 3 second.next = first 
  2 -> 1 -> 3 -> 4
  prev.next =   
  
  
  
'''
function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const o:{
        [key:string]: number
    } = {}

    for (let i = 0; i < s.length; i++){
        let char = s[i];
        if (!(char in o)){
            o[char] = 0;
        }
        o[char]++
    }


    for (let i = 0; i < t.length; i++){
        let char = t[i];
        
        if (char in o){
            o[char]--
        }
        if (o[char] === 0){
            delete o[char]
        }
    }

    return Object.keys(o).length === 0;
};
