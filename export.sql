WbExport -type=text 
         -file='table3.csv' 
--         -file='table.csv'
         -delimiter=','
         -decimal=',';

select  heart_rate.device_id, heart_rate.rri, heart_rate.tstamp from (
    select * from (
    select device_id, day, count(*) as notnullcount from
    (select device_id, trunc(tstamp) as day, rri, hr from heart_rate where rri is not null and tstamp >= date_trunc('day',getdate())-114
       and tstamp < date_trunc('day',getdate())-107
    )
    group by device_id, day

  )  order by notnullcount desc limit 5
) as topactivedevice,
heart_rate where topactivedevice.device_id=heart_rate.device_id and heart_rate.tstamp>=date_trunc('day',getdate())-114
 and heart_rate.tstamp < date_trunc('day',getdate())-107
