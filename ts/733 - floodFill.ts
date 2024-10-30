function travel(image:number[][], y: number, x: number, color:number, val: number):void {
    if (y < 0 || y >= image.length) return;
    if (x < 0 || x >= image[0].length) return;
    if (image[y][x] === color) return;
    if (image[y][x] != val) return;

    image[y][x] = color

    const dirs = [
        [0,1],
        [0,-1],
        [1,0],
        [-1,0]
    ];

    for (let [nX, nY] of Object.values(dirs)){
        travel(image, nY + y, nX + x, color, val);
    }
}

function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    travel(image, sr, sc, color, image[sr][sc]);
    return image;
};