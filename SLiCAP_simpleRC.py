from SLiCAP import *


prj = initProject('My first RC network')
instr = instruction()
instr.setCircuit('Draft2.cir')
instr.setSimType('symbolic')
instr.setSource('V1')
instr.setDetector('V_out')
instr.setGainType('gain')
instr.setDataType('laplace')
result = instr.execute()
print(result.laplace)


#          Draft2.cir

#   "my first RC network"
#   * <.asc File Location>
#   V1 N001 0 V value=1 dc=0 dcvar=0 noise=0
#   R1 N001 out {R}
#   C1 out 0 {C}
#   .param R=1k C={1/(2*pi*R*f_c)} f_c=1k
#   .backanno
#   .end
