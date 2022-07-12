<template>
    <div class="townarray">
        <h1 class="label">СПИСОК ГОРОДОВ</h1>   
        <div class="town-container">
            <div class="town-row">
                <div class="town-card">
                    <span class="title">Москва</span>
                    <div class="bottom-info">
                        <button class="ref-to-town">Смотреть</button>
                        <div class="right-info">
                            <div class="rate">Общая оценка: 5/5</div>
                            <div class="amount-of-places">Кол-во мест: 120+</div>
                        </div>
                    </div>
                </div>
                <div class="town-card">
                    <span class="title">Москва</span>
                    <div class="bottom-info">
                        <button class="ref-to-town">Смотреть</button>
                        <div class="right-info">
                            <div class="rate">Общая оценка: 5/5</div>
                            <div class="amount-of-places">Кол-во мест: 120+</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style scooped>
.townarray{
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100vh;
}
.label{
    margin-top: 2rem;
    margin-bottom: 2rem;
    align-self: center;
}
.town-container{
    padding-left: 7.5rem;
    padding-right: 7.5rem;
}
.town-row{
    display: flex;
    flex-direction: row;
}
.town-card{
    width: 50.625rem;
    height: 18.75rem;
}

</style>