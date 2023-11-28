project(
    'deez_codon',
    'cpp',
    version : '0.1',
    default_options : [
        'cpp_std=c++20',
        'warning_level=everything',
    ],
)

add_project_arguments(
    '-Wno-effc++',
    language : 'cpp',
)

arithmetic_coder = executable(
    'arithmetic-coder',
    sources : [
        './ac/tests/arithmetic-coder.cpp',
        './deez/Streams/ArithmeticCoder.cc',
    ],
    include_directories : [
        include_directories('./deez/Streams'),
    ],
)
