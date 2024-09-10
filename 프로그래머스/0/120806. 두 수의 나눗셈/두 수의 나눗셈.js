// Math.trunc()는 소수점 이하는 다 버린다. ex) Math.trunc(23.3) = 23, Math.trunc(-23.3) = -23

const solution=(num1,num2)=>Math.trunc(num1/num2 * 1000)