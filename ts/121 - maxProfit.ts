function maxProfit(prices: number[]): number {
  let localMin = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; i++){
      let price = prices[i];
      let currentProfit = price - localMin;
      maxProfit = Math.max(maxProfit, currentProfit);
      if (price < localMin){
          localMin = price;
      }
      
  }
  return maxProfit;
};