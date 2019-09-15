function numberOfBones(age) {
  bones = 412;

  if(age >= 18) {
    bones = 206;
  }

  return bones;
}

function printMessageAboutBones(bones) {
  console.log("Voce tem ", bones, " ossos");
}