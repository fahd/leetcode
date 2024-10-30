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