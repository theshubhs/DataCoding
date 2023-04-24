import pytest
import great_expectations as ge


@pytest.mark.sanity
def test_5csvfiledatacheck():
    #reading the csv files
    read_df = ge.read_csv("./DataInput/Cust_test.csv")
    
    #check 1 - validate if column exist or not
    check1= read_df.expect_column_to_exist('income')
    print('#Check1 - validate if column exist or not')
    print(f'{check1.success}',f'{check1.result}',sep='\n')
    
    #check 2 - validate column having null values
    check2 = read_df.expect_column_values_to_not_be_null('firstname', result_format = 'COMPLETE')
    print('#Check2 - validate column having null values')
    print(f'{check2.success}',f'{check2.result}',sep='\n')

    #check 3 - validate column values to be unique
    check3 = read_df.expect_column_values_to_be_unique('username')
    print('#Check 3 - validate column values to be unique')
    print(f'{check3.success}',f'{check3.result}',sep='\n')
    
    #check 4 - validate row count
    check4 = read_df.expect_table_row_count_to_equal(19998)
    print('#Check 4 - validate row count')
    print(f'{check4.success}',f'{check4.result}',sep='\n')
    
    #check 5 - validate column max value 
    check5 = read_df.expect_column_max_to_be_between('age',min_value=None, max_value =90 )
    print('#Check 5 - validate column max value')
    print(f'{check5.success}',f'{check5.result}',sep='\n')


# test_5csvfiledatacheck()

